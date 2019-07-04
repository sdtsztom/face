# -*-coding:utf-8-*-
import pymysql
import cv2
import faceBackend.faceLib.facelib as fl

db=pymysql.connect('localhost','tsz','123','faces')
cur=db.cursor()
cur.execute('select face from faceEncoding where ID=2;')
res=cur.fetchall()
imgblob=res[0][0]
img=fl.jpgBlob2img(imgblob)
db.close()
print('here')
cv2.imshow('jpg',img)
cv2.waitKey(0)