from ..faceLib import facelib as fl
from ..faceLib import facedb as fdb

def compareFaceDB(img,location=None):
    if not location:
        fFinder=fl.faceFinder();
        location=fFinder.findFaces(img)[0]
    unknown_encoding=fl.encodeFace(img,location)
    db=fdb.facedb()
    known_encodings=db.getAllEncodings()
    fl.faceDistance(known_encodings,unknown_encoding)