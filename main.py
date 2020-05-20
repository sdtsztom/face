# -*-coding:utf-8-*-

import sys
from myUI import Ui_MainWindow
from PyQt5 import QtCore,QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow
import cv2
import faceBackend as fb
from faceBackend.faceLib import facelib as fl
from faceBackend.faceLib import facedb as fdb
import time


class m_MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui=Ui_MainWindow()
		self.ui.setupUi(self)
		
		self.timerCamera0 = QtCore.QTimer()
		self.cap0 = cv2.VideoCapture()
		self.cam0Addr='http://admin:admin@192.168.43.176:8081'
		#self.cam0Addr=0
		self.camera0State=0
		self.calFpsFrameInterval=30 # 大约1s计算一次

		self.slotInit()

		self.siamBodyTracker=fb.SiamBodyTracker()
		self.db=fdb.facedb()

		self.flagCaped=False
		self.frameNum=-1
		self.QRectSquareProfile=QtCore.QRect(740, 40, 200, 200)
		self.QRectSquareInfo=QtCore.QRect(740, 250, 200, 221)
		self.QRectRecProfile=QtCore.QRect(740, 40, 200, 280)
		self.QRectRecInfo=QtCore.QRect(740, 330, 200, 141)
		
	def slotInit(self):
		self.timerCamera0.timeout.connect(self.showCamera0)

	def showCameraButtonClicked(self):
		if self.timerCamera0.isActive() == False:
			flag = self.cap0.open(self.cam0Addr)
			if flag == False:
				QtWidgets.QMessageBox.warning(self, "Warning", "请检测相机与电脑是否连接正确")
			else:
				self.timerCamera0.start(30) # ms,about 30fps
				self.ui.buttonSwitchCamera.setText('停止')
				self.siamBodyTracker.setWantIDs(-1)  # track all people in the database
		else:
			self.timerCamera0.stop()
			self.cap0.release()
			self.ui.labelCamera0.clear()
			self.ui.labelProfile.clear()
			self.ui.buttonSwitchCamera.setText('开始')
			self.ui.labelInfo.setText('信息：')
			self.ui.labelFPS.setText('帧率：')
			self.siamBodyTracker.reset()
			self.frameNum=-1
			self.tic=self.toc=0
			self.flagCaped=False
		
	def showCamera0(self):
		# 计算与显示帧率
		self.frameNum=(self.frameNum+1)%self.calFpsFrameInterval
		if self.frameNum==0:
			self.tic=time.time()
		elif self.frameNum==self.calFpsFrameInterval-1:
			self.toc=time.time()
			interval=self.toc-self.tic
			self.ui.labelFPS.setText('帧率：%f fps'%(self.calFpsFrameInterval/interval))

		flag, image = self.cap0.read()  # cv2 img h*w*bgr

		# 开始追踪
		info=self.siamBodyTracker.track(image, firstFrameReturn='infos')    # 暂时只能追踪一个人，所以返回的是info而非infos
		if not self.flagCaped and type(info)==list: # 两元组，[id,location]，表示发现第一次了与数据库中人员匹配的人脸
			id,location=info
			self.flagCaped=True
			image = fl.drawBox(image, location)

			# 显示肖像
			faceImg=fl.cropFace(image,location)
			h,w,_=faceImg.shape
			print('profile ratio:',h/w)
			self.adjustLayout(h/w)
			self.showCV2CapRawImage(self.ui.labelProfile,faceImg)

			# 显示信息
			personInfo=self.db.getCustomOneLineInfo('select name,sex,institute,major from faceEncoding where ID=%d;'%(id))   # personInfo=[name]
			self.ui.labelInfo.setText('姓名：'+personInfo[0]+'\n性别：'+personInfo[1]+'\n学院：'+personInfo[2]+'\n专业：'+personInfo[3])

		self.showCV2CapRawImage(self.ui.labelCamera0,image)

	def adjustLayout(self,hwRatio):
		ratioSquare=1
		ratioRec=7.0/5
		if abs(hwRatio-ratioSquare)>abs(hwRatio-ratioRec):
			use='Rec'
		else:
			use='Square'
		if use=='Rec':
			self.ui.labelProfile.setGeometry(self.QRectRecProfile)
			self.ui.labelInfo.setGeometry(self.QRectRecInfo)
		else:
			self.ui.labelProfile.setGeometry(self.QRectSquareProfile)
			self.ui.labelInfo.setGeometry(self.QRectSquareInfo)

	def showCV2CapRawImage(self,label,rawImage):
		_,_,w,h=label.geometry().getRect() # geometry() return QRect
		img = cv2.resize(rawImage, (w, h))
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		Qimg = QtGui.QImage(img.data, img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888)
		label.setPixmap(QtGui.QPixmap.fromImage(Qimg))

app=QApplication(sys.argv)
main_window = m_MainWindow()
main_window.show()
sys.exit(app.exec_())