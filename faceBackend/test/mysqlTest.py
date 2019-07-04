# -*-coding:utf-8-*-
import pymysql
import numpy as np

db=pymysql.connect('localhost','tsz','123','faces')
cur=db.cursor()

insertArray=True
if insertArray:
	cur.execute('update faceEncoding set encoding=%s where ID=1;',(np.load('encoding.npy').tostring()))
	db.commit()

cur.execute('select encoding from faceEncoding where ID=1;')
res=cur.fetchall();
encoding=res[0][0]
db.close()
print(type(encoding),encoding)
data=np.frombuffer(encoding,dtype='float64')
print(data)