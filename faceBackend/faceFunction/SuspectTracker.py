from ..faceLib import facelib as fl
from ..faceLib import facedb as fdb
from ..faceLib import util
import os.path as path

class FaceTracker(object):
    def __init__(self,wantIDs,save_path,use_scale=True,scale_xy=0.5):
        self.wantIDs=wantIDs
        self.captured=[False]*len(wantIDs)

        self.save_path=save_path
        self.use_scale=use_scale
        self.scale_xy=scale_xy
        self.fFinder=fl.faceFinder(self.use_scale,self.scale_xy)

        db=fdb.facedb()
        self.wantEncodings=db.getEncodingsByIDs(wantIDs)
        db.close()

    def track(self,frame):
        locations=self.fFinder.findFaces(frame)
        unknown_encodings=fl.encodeFaces(frame,locations)
        judged_index_in_wantIDs=self.compare(unknown_encodings)
        #self.capture(judged_index_in_wantIDs,frame,locations)
        drawLocations=[locations[i] for i in len(locations) if judged_index_in_wantIDs[i]!=-1]
        return fl.drawBoxes(frame,drawLocations)

    def compare(self, unknown_encodings):
        judged_index_in_wantIDs=[-1]*len(unknown_encodings)
        for i,unknown_encoding in enumerate(unknown_encodings):
            res=fl.faceCompare(self.wantEncodings,unknown_encoding)
            if True in res:
                judged_index_in_wantIDs[i]=res.index(True)
        return judged_index_in_wantIDs

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