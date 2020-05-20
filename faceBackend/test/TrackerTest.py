import faceBackend as fb
import faceBackend.faceLib.facelib as fl
import faceBackend.faceLib.facedb as fdb
import cv2

cap=cv2.VideoCapture()
cap.open('../auxiliary/test.mp4')
ret,img=cap.read()
cv2.imshow('test',img)
cv2.waitKey(0) # necessary or will not show img

bodyTracker=fb.SiamBodyTracker()
bodyTracker.setWantIDs(-1)
for i in [1,2,3]:
	info=bodyTracker.track(img,firstFrameReturn='infos')
	if type(info)==list:
		print(info)
	else:
		print(type(info))