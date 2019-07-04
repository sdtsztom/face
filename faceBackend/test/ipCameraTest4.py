import cv2
import numpy as np
import os

cap=cv2.VideoCapture('rtsp://192.168.1.100:8080/h264_ulaw.sdp')

while True:
	ret,frame=cap.read()
	if not ret or cv2.waitKey(1)==ord('q'):
		break
	else:
		cv2.imshow('frame',frame)

cap.release()
cv2.destroyAllWindows()