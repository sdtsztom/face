from ..faceLib import facelib as fl
import random

class EmotionRecognizer(object):
    def __init__(self):
        self.recog=fl.facialExpressionRecer()
        self.supportEmotion=self.class_names = ['Angry','Happy','Sad', 'Surprise','Neutral']
        self.EmotionPool=self.supportEmotion
        self.fFinder=fl.faceFinder()
    def getSupportEmotion(self):
        return self.supportEmotion
    def genRandomRequireEmotion(self):
        return self.EmotionPool.pop(random.randrange(1,len(self.EmotionPool)))
    def reset(self):
        self.EmotionPool=self.supportEmotion
    def getEmotion(self,frame,expectEmotion=None):
        locations=self.fFinder.findFaces(frame)
        if locations:
            location=locations[0]
            face=fl.cropFace(frame,location)
            if expectEmotion is None:
                return self.recog.predict(face)
            else:
                return expectEmotion==self.recog.predict(face)
        else:
            return False
