import cv2
import numpy as np
from ..faceFunction.SuspectTracker import Tracker

tracker=Tracker('')

first=True

cap=cv2.VideoCapture(0)
while True:
	ret,frame=cap.read()
	if not ret or not first or cv2.waitKey(1)==ord('q'):
		break
	else:
		cv2.imshow('frame',frame)
		tracker.detecTrack(frame)
		first=False

cap.release()
cv2.destroyAllWindows()