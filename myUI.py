# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './SequnceSecurity.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(956, 559)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.labelCamera0 = QtWidgets.QLabel(self.centralwidget)
        self.labelCamera0.setGeometry(QtCore.QRect(30, 40, 680, 480))
        self.labelCamera0.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelCamera0.setText("")
        self.labelCamera0.setObjectName("labelCamera0")
        self.buttonSwitchCamera = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSwitchCamera.setGeometry(QtCore.QRect(800, 490, 89, 25))
        self.buttonSwitchCamera.setObjectName("buttonSwitchCamera")
        self.labelInfo = QtWidgets.QLabel(self.centralwidget)
        self.labelInfo.setGeometry(QtCore.QRect(740, 330, 200, 141))
        self.labelInfo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelInfo.setObjectName("labelInfo")
        self.labelProfile = QtWidgets.QLabel(self.centralwidget)
        self.labelProfile.setGeometry(QtCore.QRect(740, 40, 200, 280))
        self.labelProfile.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.labelProfile.setText("")
        self.labelProfile.setObjectName("labelProfile")
        self.labelFPS = QtWidgets.QLabel(self.centralwidget)
        self.labelFPS.setGeometry(QtCore.QRect(30, 10, 150, 17))
        self.labelFPS.setObjectName("labelFPS")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.buttonSwitchCamera.clicked.connect(MainWindow.showCameraButtonClicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sequence智防"))
        self.buttonSwitchCamera.setText(_translate("MainWindow", "开始"))
        self.labelInfo.setText(_translate("MainWindow", "信息："))
        self.labelFPS.setText(_translate("MainWindow", "帧率："))
