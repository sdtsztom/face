from ..faceLib import facelib as fl
import random

class EmotionRecognizer(object):
    def __init__(self):
        self.recog=fl.facialExpressionRecer()
        self.supportEmotion=self.class_names = ['Angry','Happy','Sad', 'Surprise', 'Neutral']
        self.EmotionPool=self.supportEmotion
    def getSupportEmotion(self):
        return self.supportEmotion
    def genRandomRequireEmotion(self):
        return self.EmotionPool.pop(random.randrange(1,len(self.supportEmotion)))
    def reset(self):
        self.EmotionPool=self.supportEmotion
    def getEmotion(self,frame,expectEmotion=None):
        if expectEmotion is None:
            return self.recog.predict(frame)
        else:
            return expectEmotion==self.recog.predict(frame)
