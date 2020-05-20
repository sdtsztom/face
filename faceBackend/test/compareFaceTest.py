import faceBackend as fb
import faceBackend.faceLib.facelib as fl
import faceBackend.faceLib.facedb as fdb
import cv2

img=cv2.imread('../auxiliary/test.jpg')
fFinder = fl.faceFinder()
location = fFinder.findFaces(img)[0]
unknown_encoding = fl.encodeFace(img, location)
db = fdb.facedb()
known_encodings = db.getAllEncodings()
res=fl.faceCompare(known_encodings,unknown_encoding)
print(res)