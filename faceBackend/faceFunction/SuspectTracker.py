from ..faceLib import facelib as fl
from ..faceLib import facedb as fdb
from ..faceLib import util
import numpy as np

class FaceTracker(object):
    # able to track multiple people
    def __init__(self,wantIDs=None,use_scale=True,scale_xy=0.25):
        '''
        :param wantIDs: 1. list,means ids of people want to track
                        2. -1,means track all the people in the database
        '''
        self.setWantIDs(wantIDs)

        self.use_scale=use_scale
        self.scale_xy=scale_xy
        self.fFinder=fl.faceFinder(self.use_scale,self.scale_xy)

    def setWantIDs(self,wantIDs):
        # TODO 这个函数在对比所有数据的实现上比较应付，待改善
        self.wantIDs = wantIDs
        if wantIDs is not None:
            db = fdb.facedb()
            if wantIDs==-1:
                self.wantEncodings = db.getAllEncodings()  # 这里没加参数，因为测试数据库数据量小，可以直接取出所有数据
                self.wantIDs = range(1, len(self.wantEncodings) + 1)
                self.captured = [False] * len(self.wantEncodings)
            else:
                self.wantEncodings = db.getAllEncodings(wantIDs)
                self.captured=[False]*len(wantIDs)
            db.close()

    def reset(self):
        self.wantIDs=None
        self.wantEncodings=None

    def track(self, frame, returnType='frame'):
        '''
        函数本质为detect，在每帧detect指定人员人脸
        :returnType: 有infos,locations,frame三种
        '''
        locations=self.fFinder.findFaces(frame)
        unknown_encodings=fl.encodeFaces(frame,locations)
        ID_of_unknownfaces=self.compare(unknown_encodings)
        #self.capture(judged_index_in_wantIDs,frame,locations)
        drawLocations=[locations[i] for i in range(len(locations)) if ID_of_unknownfaces[i]!=-1]    # 筛选出属于wantIDs中的人脸
        if returnType== 'infos':
            info = [[ID_of_unknownfaces[i],locations[i]] for i in range(len(locations)) if ID_of_unknownfaces[i] != -1]
            return info
        elif returnType== 'locations':
            return drawLocations
        elif returnType== 'frame':
            return fl.drawBoxes(frame,drawLocations)

    def compare(self, unknown_encodings):
        ID_of_unknownfaces=[-1]*len(unknown_encodings)
        for i,unknown_encoding in enumerate(unknown_encodings): # 在图中的各个未知人脸中列举
            res=fl.faceCompare(self.wantEncodings,unknown_encoding)
            if True in res:
                ID_of_unknownfaces[i]=self.wantIDs[res.index(True)]  # TODO 获取unknow face在数据库中对应的ID，待验证
        return ID_of_unknownfaces

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
    # only support track one person
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
            locations=self.faceTracker.track(frame,'locations')
            if locations:
                location=locations[0]   # 只支持追踪一个人，因此追踪第一个
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
    # only support track one person
    def __init__(self,wantIDs=None,use_scale=False,scale_xy=0.25,detectInterval=3):
        self.faceTracker=FaceTracker(wantIDs,use_scale,scale_xy)
        self.siamTracker=fl.siamTracker()
        self.siamTracker.loadModel()
        self.peopleDetecter=fl.personDetecter()
        self.detected=False
        self.tic=0
        self.detectInterval=detectInterval

    def setWantIDs(self,wantIDs):
        self.faceTracker.setWantIDs(wantIDs)

    def track(self,frame,firstFrameReturn='frame'):
        '''
        :firstFrameReturn: 有infos,locations,frame三种
        '''
        location=None
        locations=None
        self.tic = (self.tic + 1) % self.detectInterval
        if not self.detected and not self.tic:
            if firstFrameReturn=='infos':
                infos=self.faceTracker.track(frame,'infos')
                locations=[infos[i][1] for i in range(len(infos))]
            else:
                locations=self.faceTracker.track(frame,'locations')
            if locations:
                print('SiamBodyTracker: recognized!')
                top,right,bottom,left=locations[0]  # TODO 只支持追踪一个人，因此追踪第一个
                self.detected=True
                peopleRects=self.peopleDetecter.findPeople(frame)
                peopleRects=[rect[:4] for rect in peopleRects]# 最后一个为概率
                overlaps=self.Overlaps([left,top,right,bottom],peopleRects)
                indexBiggestOverlap=np.array(overlaps).argsort()[-1]
                left,top,right,bottom=peopleRects[indexBiggestOverlap]
                location=[top,right,bottom,left]
                self.siamTracker.init(frame,left,top,right-left,bottom-top)
                if firstFrameReturn=='frame':
                    return fl.drawBox(frame, location)
                elif firstFrameReturn=='locations':
                    return location[0]  # TODO 因为暂时只支持追踪1个，所以只返回一个location
                elif firstFrameReturn=='infos':
                    return infos[0]
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

