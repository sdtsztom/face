import faceBackend as fb
import cv2

img=cv2.imread('../auxiliary/Tang2.jpg')
info=fb.faceIdentification(img)
print(info)