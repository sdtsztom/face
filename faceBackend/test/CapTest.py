import cv2
import numpy as np
from faceLib import *

ff=faceFinder()

first=True

cap=cv2.VideoCapture(0)
while True:
	ret,frame=cap.read()
	if not ret or cv2.waitKey(1)==ord('q'):
		break
	else:
		# if first:
		# 	print(type(frame[0][0][0]),frame.shape)
		# 	first=False
		cv2.imshow('frame',frame)
		locations=ff.findFaces(frame)
		if first and len(locations)==1:
			print(locations[0])
			first=False
		if locations and len(locations)==1 and first:
			encoding=encodeFace(frame,locations[0])
			print(encoding)
			np.save('encoding.npy',encoding)
			first=False


cap.release()
cv2.destroyAllWindows()