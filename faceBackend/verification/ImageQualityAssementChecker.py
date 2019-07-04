import faceBackend as fb
import cv2

img=cv2.imread('../auxiliary/shot.jpg')
imageAss=fb.ImageQualityAssement()
score=imageAss.assement(img)
print(score)