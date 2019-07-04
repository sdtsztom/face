from ..faceLib import facedb as fdb
from ..faceLib import facelib as fl

def genEncodings():
    db=fdb.facedb()
    todoIDs=db.getUnencodedIDs()
    # 为数据规模考量，暂不支持批量encode
    fFinder=fl.faceFinder()
    for ID in todoIDs:
        faceBlob=db.getFaceByID(ID)
        faceImg=fl.jpgBlob2img(faceBlob)
        locations=fFinder.findFaces(faceImg)
        encoding=fl.encodeFace(faceImg,locations[0])
        db.recordEncoding(ID,encoding)