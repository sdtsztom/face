from ..faceLib import facelib as fl
from ..faceLib import facedb as fdb
import numpy as np

def compareFaceDB(img,location=None):
    if not location:
        fFinder=fl.faceFinder();
        location=fFinder.findFaces(img)[0]
    unknown_encoding=fl.encodeFace(img,location)
    db=fdb.facedb()
    known_encodings=db.getAllEncodings()
    distances=fl.faceDistance(known_encodings,unknown_encoding)
    CandidatesIndex=distances.argsort()[:5]
    CandidatesInfo=db.getPeopleInfoByIndexes(CandidatesIndex)
    info=[[CandidatesInfo[i][0],CandidatesInfo[i][1],distances[index]] for i,index in enumerate(CandidatesIndex)]   #info:[ID,name,distance]
    return info