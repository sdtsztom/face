from ..faceLib import facelib as fl
import random

class EmotionRecognizer(object):
    def __init__(self):
        self.recog=fl.facialExpressionRecer()
        self.supportEmotion=self.class_names = ['Angry','Happy','Sad', 'Surprise','Neutral']
        self.EmotionPool=self.supportEmotion.copy()
        self.fFinder=fl.faceFinder()
        self.numTimeLimit=30    # 大约每个表情10次机会，5秒左右
        self.recgFrameInterval=15 # 推荐每隔15帧检测一次
        self.TimeLeft=self.numTimeLimit

    def getSupportEmotion(self):
        return self.supportEmotion

    def getNumTimeLimit(self):
        return self.numTimeLimit

    def getRecgFrameInterval(self):
        return self.recgFrameInterval

    def setNumTimeLimit(self,numTimeLimit):
        self.numTimeLimit=numTimeLimit

    def setRecgFrameInterval(self,recgFrameInterval):
        self.recgFrameInterval=recgFrameInterval

    def genRandomRequireEmotion(self):
        return self.EmotionPool.pop(random.randrange(1,len(self.EmotionPool)))

    def reset(self):
        self.EmotionPool=self.supportEmotion.copy()
        self.TimeLeft=self.numTimeLimit

    def checkEmotion(self, frame, expectEmotion=None,useTimeLimit=True):
        if useTimeLimit:
            self.TimeLeft-=1
            if self.TimeLeft<0:
                return 'error:Time use out!'  # 超时错误
        locations=self.fFinder.findFaces(frame)
        if locations:
            location=locations[0]
            face=fl.cropFace(frame,location)
            if expectEmotion is None:
                return self.recog.predict(face) # 没有传入expectEmotion的情况下，返回预测出的表情
            else:
                return expectEmotion==self.recog.predict(face)  # 有传入expectEmotion的情况下，返回bool判断
        else:
            return False    # 没有检测到人脸的情况下，返回False
