# -*-coding:utf-8-*-
import pymysql
import numpy as np
import cv2
import faceBackend.faceLib.facelib as fl

db=pymysql.connect('localhost','tsz','123','faces')
cur=db.cursor()

img=cv2.imread('Tang.jpg')
imgblob=fl.img2jpgBlob(img)
cur.execute('update faceEncoding set face=%s where ID=1;',(imgblob))
db.commit()
db.close()