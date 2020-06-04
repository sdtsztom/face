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

