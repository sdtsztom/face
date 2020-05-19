import pymysql
import cv2
import faceBackend.faceLib.facelib as fl

db=pymysql.connect('localhost','tsz','123','faces')
cur=db.cursor()
# imgBlob=fl.img2jpgBlob(cv2.imread('./test.jpg'))
with open('test.jpg','rb') as f:
	imgBlob=f.read()

# cur.execute('update faceEncoding set face=%s where ID=7;'%(pymysql.Binary(imgBlob)))
cur.execute('update faceEncoding set face=%s where ID=7;',imgBlob)
db.commit() # necessary!!!
cur.close()
db.close()