import faceBackend as fb
import cv2

img=cv2.imread('../auxiliary/Tang2.jpg')
caper=fb.faceCaper()
img2=caper.cap(img)
cv2.imshow('img',img2)
cv2.waitKey(0)
caper.save()