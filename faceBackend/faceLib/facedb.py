# -*-coding:utf-8-*-
import pymysql
import numpy as np

class facedb(object):
	def __init__(self,ip='localhost',user='tsz',pwd='123'):
		self._connect=True
		self.conn=pymysql.connect('localhost','tsz','123','faces')
		self.cur=self.conn.cursor()

	def close(self):
		if self._connect==True:
			self.cur.close()
			self.conn.close()
			self._connect=False

	def connect(self):
		if self._connect==False:
			self.__init__()
			self._connect=True

	# def insert(self,name,img,encoding):
	# 	self.cur.execute('insert into faceEncoding(name,face,encoding) values(%s,%s,%s);',(name,img,encoding.tostring()))
	# 	self.conn.commit()

	def getAllEncodings(self):
		self.cur.execute('select encoding from faceEncoding;')
		res=self.cur.fetchAll()
		encodings=[np.frombuffer(res[i][0],dtype='float64') for i in range(len(res))]
		return encodings

	def getEncodingsByIDs(self,IDList):
		self.cur.execute('select encoding from faceEncoding where ID in %s;'%(str(tuple(IDList))));
		res=self.cur.fetchall()
		encodings = [np.frombuffer(res[i][0], dtype='float64') for i in range(len(IDList))]
		return encodings

	def getUnencodedIDs(self):
		self.cur.execute('select ID from faceEncoding where encoded=0')
		res=self.cur.fetchall()
		UnencodedIDs=[int(res[i][0]) for i in range(len(res))]
		return UnencodedIDs

	def getFaceByID(self,ID):
		self.cur.execute('select face from faceEncoding where ID=%d'%(ID))
		res = self.cur.fetchall()
		return res[0][0]

	def recordEncoding(self,ID,encoding):
		temp='ID=%d;'%(ID)
		sql='insert into faceEncoding(encoding) values(%s) where '+temp
		self.cur.execute('update faceEncoding set encoding=%s,encoded=1 where '+temp,(encoding.tostring()))
		self.conn.commit()