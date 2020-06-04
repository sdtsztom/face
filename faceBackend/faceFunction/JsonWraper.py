from . import SuspectTracker
from . import CompareFace
from . import faceCaper
from . import GenEncodings
from . import EmotionRecognizer
from . import ImageQualityAssement
import json

def genEncodings():
	res=GenEncodings.genEncodings()
	res={'numEncoded':res}
	return json.dumps(res)

def faceIdentification(img, location=None):
	infos=CompareFace.faceIdentification(img, location)
	res={}
	for i,info in enumerate(infos):
		res['person%d'%(i)]={'ID':info[0],'name':info[1],'dis':info[2]}
	return json.dumps(res)

def faceVerification(imgList):
	flag = CompareFace.faceVerification(imgList)
	res={'Same':flag}
	return json.dumps(res)

class ImageQualityAssementJson(ImageQualityAssement):
	def __init__(self):
		super().__init__()

	def assement(self,img):
		score=super().assement(img)
		res={'score':score}
		return json.dumps(res)