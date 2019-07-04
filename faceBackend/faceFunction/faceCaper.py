from ..faceLib import facelib as fl
import os.path as path

class faceCaper(object):
    def __init__(self):
        self.img=0
        self.locations=0

    def cap(self,img):
        self.img=img
        fFinder=fl.faceFinder()
        self.locations=fFinder.findFaces(img)
        img=fl.drawBoxes(img,self.locations)
        return img

    def save(self, savepath='.'):
        savepaths=[path.join(savepath, 'face%d.jpg' % (i)) for i in range(len(self.locations))]
        fl.recordFaces(self.img, self.locations, savepaths)