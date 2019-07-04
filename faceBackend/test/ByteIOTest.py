import cv2
import io
import numpy as np

a=cv2.imread('test.jpg');
print(a)
print('*****************************************')

is_success,buffer=cv2.imencode('.jpg',a)
bio=io.BytesIO(buffer)
b=bio.read()
print(b)

a_=cv2.imdecode(np.frombuffer(b,np.int8),-1)
cv2.imshow('a_',a_)
cv2.waitKey(0)