import faceBackend.faceLib.facelib as fl
import cv2

facialRecer = fl.facialExpressionRecer()
fFinder=fl.faceFinder()
cap=cv2.VideoCapture('../auxiliary/output.mp4')
frameNum=0
while True:
	ret,frame=cap.read()
	if not ret or cv2.waitKey(1)==ord('q'):
		break
	else:
		frameNum+=1
		if frameNum%10==0:
			locations=fFinder.findFaces(frame)
			if locations:
				face=fl.cropFace(frame,locations[0])
				mood=facialRecer.predict(face)
				print(mood)

		cv2.imshow('frame',frame)

cap.release()
cv2.destroyAllWindows()

# img=cv2.imread('../auxiliary/angry.jpg')
# mood=facialRecer.predict(img)
# print(mood)
# img=cv2.imread('../auxiliary/surprise.jpg')
# mood=facialRecer.predict(img)
# print(mood)
# img=cv2.imread('../auxiliary/neutral.jpg')
# mood=facialRecer.predict(img)
# print(mood)
