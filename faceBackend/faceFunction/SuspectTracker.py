from ..faceLib import facelib as fl
from ..faceLib import facedb as fdb
from ..faceLib import util

class FaceTracker(object):
    def __init__(self,wantIDs,use_scale=True,scale_xy=0.25):
        self.wantIDs=wantIDs
        self.captured=[False]*len(wantIDs)

        self.use_scale=use_scale
        self.scale_xy=scale_xy
        self.fFinder=fl.faceFinder(self.use_scale,self.scale_xy)

        db=fdb.facedb()
        self.wantEncodings=db.getEncodingsByIDs(wantIDs)
        db.close()

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
    def __init__(self,wantIDs,use_scale=True,scale_xy=0.25):
        self.faceTracker=FaceTracker(wantIDs,use_scale,scale_xy)
        self.siamTracker=fl.siamTracker()
        self.siamTracker.loadModel()
        self.detected=False

    def track(self,frame):
        if not self.detected:
            locations=self.faceTracker.track(frame,True)
            if locations:
                location=locations[0]
                top,right,bottom,left=location
                self.detected=True
                self.siamTracker.init(frame,left,top,right-left,bottom-top)
        else:
            location=self.siamTracker.track(frame)
        return fl.drawBox(frame, location)
