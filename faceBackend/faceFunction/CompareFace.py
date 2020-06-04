from ..faceLib import facelib as fl
from ..faceLib import facedb as fdb
import numpy as np

def faceSearchCompare(img, location=None):
    '''
    :param location: style: [left,right,bottom,left]
    '''
    if not location:
        fFinder=fl.faceFinder()
        location=fFinder.findFaces(img)[0]
    unknown_encoding=fl.encodeFace(img,location)
    db=fdb.facedb()
    known_encodings=db.getAllEncodings()
    distances=fl.faceDistance(known_encodings,unknown_encoding)
    CandidatesIndex=distances.argsort()[:5]
    CandidatesInfo=db.getPeopleInfosByIndexes(CandidatesIndex)
    infos=[[CandidatesInfo[i][0],CandidatesInfo[i][1],distances[index]] for i,index in enumerate(CandidatesIndex)]   #info:[ID,name,distance]
    return infos

def faceCheckCompare(imgList):
    fFinder = fl.faceFinder()
    encodings=[0]*len(imgList)
    for i,img in enumerate(imgList):
        location=fFinder.findFaces(img)[0]
        encodings[i]=fl.encodeFace(img, location)
    flag_all_pass=True
    for encoding in encodings:
        res=fl.faceCompare(encodings,encoding)
        flag_all_pass=np.all(res)
        if not flag_all_pass:
            break
    return flag_all_pass