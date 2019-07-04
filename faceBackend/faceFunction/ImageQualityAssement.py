import faceBackend.faceLib.facelib as fl

class ImageQualityAssement(object):
    def __init__(self):
        self.modelpath="/media/tsz/Data/Work/Tracking/GithubProject/No-Reference-Image-Quality-Assessment-using-BRISQUE-Model/Python/libsvm/python/allmodel"

    def assement(self,img):
        return fl.imageQualityAssement(self.modelpath,img)