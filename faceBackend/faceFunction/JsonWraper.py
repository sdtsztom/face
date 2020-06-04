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

def faceSearchCompare(img, location=None):
	infos=CompareFace.faceSearchCompare(img,location)
	res={}
	for i,info in enumerate(infos):
		res['person%d'%(i)]={'ID':info[0],'name':info[1],'dis':info[2]}
	return  res