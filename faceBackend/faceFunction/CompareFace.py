from ..faceLib import facelib as fl
from ..faceLib import facedb as fdb
import numpy as np

def faceIdentification(img, location=None):
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

def faceVerification(imgList):
    fFinder = fl.faceFinder()
    encodings=[0]*len(imgList)
    for i,img in enumerate(imgList):
        location=fFinder.findFaces(img)[0]
        encodings[i]=fl.encodeFace(img, location)
    res=fl.faceCompare(encodings,encodings[0])
    flag_all_pass=np.all(res)
    return bool(flag_all_pass)  # 转化为python内置bool类型，容错率更高