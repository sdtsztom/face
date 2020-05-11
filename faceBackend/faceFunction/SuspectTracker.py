from ..faceLib import facelib as fl
from ..faceLib import facedb as fdb
from ..faceLib import util
import numpy as np

class FaceTracker(object):
    def __init__(self,wantIDs=None,use_scale=True,scale_xy=0.25):
        self.setWantIDs(wantIDs)

        self.use_scale=use_scale
        self.scale_xy=scale_xy
        self.fFinder=fl.faceFinder(self.use_scale,self.scale_xy)

    def setWantIDs(self,wantIDs):
        if wantIDs is not None:
            self.wantIDs = wantIDs
            self.captured=[False]*len(wantIDs)
            db = fdb.facedb()
            self.wantEncodings = db.getEncodingsByIDs(wantIDs)
            db.close()

    def reset(self):
        self.wantIDs=None
        self.wantEncodings=None

    def track(self,frame,returnLocations=False):
        locations=self.fFinder.findFaces(frame)
        unknown_encodings=fl.encodeFaces(frame,locations)
        ID_of_unknownface=self.compare(unknown_encodings)
        #self.capture(judged_index_in_wantIDs,frame,locations)
        drawLocations=[locations[i] for i in range(len(locations)) if ID_of_unknownface[i]!=-1]
        if returnLocations:
            return drawLocations
        else:
            return fl.drawBoxes(frame,drawLocations)

    def compare(self, unknown_encodings):
        ID_of_unknownface=[-1]*len(unknown_encodings)
        for i,unknown_encoding in enumerate(unknown_encodings):
            res=fl.faceCompare(self.wantEncodings,unknown_encoding)
            if True in res:
                ID_of_unknownface[i]=res.index(True)
        return ID_of_unknownface

    # def capture(self,judged_index_in_wantIDs,frame,locations):
    #     for i,want_index in enumerate(judged_index_in_wantIDs):
    #         if want_index!=-1 and self.captured[want_index]==False:
    #             fl.recordFace(frame,locations[i],path.join(self.save_path,'%d.jpg'%(self.wantIDs[want_index])))

class DetectTracker(object):
    def __init__(self,save_path):
        self.person_detecter=fl.personDetecter()

    def track(self,frame):
        people_boxes=self.person_detecter.findPeople(frame)
        people_locations=util.boxes2locations(people_boxes)
        return util.drawBox(frame,people_locations)

class SiamFaceTracker(object):
    def __init__(self,wantIDs=None,use_scale=True,scale_xy=0.25,detectInterval=10):
        self.faceTracker=FaceTracker(wantIDs,use_scale,scale_xy)
        self.siamTracker=fl.siamTracker()
        self.siamTracker.loadModel()
        self.detected=False
        self.tic=0
        self.detectInterval=detectInterval

    def setWantIDs(self, wantIDs):
        self.faceTracker.setWantIDs(wantIDs)

    def track(self,frame):
        location=None
        locations=None
        self.tic=(self.tic+1)%self.detectInterval
        if not self.detected and not self.tic:
            locations=self.faceTracker.track(frame,True)
            if locations:
                location=locations[0]
                top,right,bottom,left=location
                self.detected=True
                self.siamTracker.init(frame,left,top,right-left,bottom-top)
                return fl.drawBox(frame, location)
        if self.detected:
            location=self.siamTracker.track(frame)
            return fl.drawBox(frame, location)
        else:
            return frame

    def reset(self):
        self.detected=False
        self.tic=0
        self.faceTracker.reset()


class SiamBodyTracker(object):
    def __init__(self,wantIDs=None,use_scale=False,scale_xy=0.25,detectInterval=10):
        self.faceTracker=FaceTracker(wantIDs,use_scale,scale_xy)
        self.siamTracker=fl.siamTracker()
        self.siamTracker.loadModel()
        self.peopleDetecter=fl.personDetecter()
        self.detected=False
        self.tic=0
        self.detectInterval=detectInterval

    def setWantIDs(self,wantIDs):
        self.faceTracker.setWantIDs(wantIDs)

    def track(self,frame):
        location=None
        locations=None
        self.tic = (self.tic + 1) % self.detectInterval
        if not self.detected and not self.tic:
            locations=self.faceTracker.track(frame,True)
            if locations:
                print('recognized')
                top,right,bottom,left=locations[0]
                self.detected=True
                peopleRects=self.peopleDetecter.findPeople(frame)
                peopleRects=[rect[:4] for rect in peopleRects]# 最后一个为概率
                overlaps=self.Overlaps([left,top,right,bottom],peopleRects)
                indexBiggestOverlap=np.array(overlaps).argsort()[-1]
                left,top,right,bottom=peopleRects[indexBiggestOverlap]
                location=[top,right,bottom,left]
                self.siamTracker.init(frame,left,top,right-left,bottom-top)
                return fl.drawBox(frame, location)
        if self.detected:
            location=self.siamTracker.track(frame)
            return fl.drawBox(frame, location)
        else:
            return frame

    def Overlaps(self, faceRect, BodyRects):
        overlaps=[0]*len(BodyRects)
        for i,bodyRect in enumerate(BodyRects):
            if util.checkIntersect(faceRect, bodyRect):
                overlaps[i]=util.Overlap(faceRect, bodyRect)
        return overlaps

    def reset(self):
        self.detected=False
        self.tic=0
        self.faceTracker.reset()

