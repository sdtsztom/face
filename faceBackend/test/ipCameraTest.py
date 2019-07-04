import cv2
import numpy as np

ip='192.168.1.100'
port='8081'
video="http://admin:admin@"+ip+':'+port
cap=cv2.VideoCapture(video)

while True:
	ret,frame=cap.read()
	if not ret or cv2.waitKey(1)==ord('q'):
		break
	else:
		cv2.imshow('frame',frame)

cap.release()
cv2.destroyAllWindows()