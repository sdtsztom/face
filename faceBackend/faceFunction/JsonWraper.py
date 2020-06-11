from . import SuspectTracker
from . import CompareFace
from . import faceCaper
from . import GenEncodings
from . import EmotionRecognizer
from . import ImageQualityAssement
import json

def genEncodings():
	res=GenEncodings.genEncodings()
	res={'numEncoded':res}
	return json.dumps(res)

def faceIdentification(img, location=None):
	infos=CompareFace.faceIdentification(img, location)
	res={}
	for i,info in enumerate(infos):
		res['person%d'%(i)]={'ID':info[0],'name':info[1],'dis':info[2]}
	return json.dumps(res)

def faceVerification(imgList,detail=False):
	res = CompareFace.faceVerification(imgList,detail)
	res={'same':res}
	return json.dumps(res)

class ImageQualityAssement(ImageQualityAssement.ImageQualityAssement):
	def __init__(self):
		super().__init__()

	def assement(self,img):
		score=super().assement(img)
		res={'score':score}
		return json.dumps(res)

class EmotionRecognizer(EmotionRecognizer.EmotionRecognizer):
	def __init__(self):
		super().__init__()

	def getSupportEmotion(self):
		return super().getSupportEmotion()

	def getNumTimeLimit(self):
		return super().getNumTimeLimit()

	def getRecgFrameInterval(self):
		return super().getRecgFrameInterval()

	def setNumTimeLimit(self, numTimeLimit):
		super().setNumTimeLimit(numTimeLimit)

	def setRecgFrameInterval(self, recgFrameInterval):
		super().setRecgFrameInterval(recgFrameInterval)

	def genRandomRequireEmotion(self):
		return super().genRandomRequireEmotion()

	def reset(self):
		super().reset()

	def checkEmotion(self, frame, expectEmotion=None, useTimeLimit=True):
		res={}
		ret=super().checkEmotion(frame, expectEmotion, useTimeLimit)
		if type(ret)==str and ret.startswith('error'):  # 超时错误
			res['error']=ret
		else:   # 预测结果
			res['predict']=ret
		if type(ret)==bool: # 返回确认结果
			res['pass']=ret
		return json.dumps(res)