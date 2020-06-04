import faceBackend.faceLib.facelib as fl
from .FunctionConfig import FunctionConfig

class ImageQualityAssement(object):
    def __init__(self):
        self.modelpath=FunctionConfig.ImageQualAssConfig['modelPath']

    def assement(self,img):
        return fl.imageQualityAssement(self.modelpath,img)