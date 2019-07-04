import faceBackend as fb
import cv2

tracker=fb.FaceTracker([1],True,0.25)
cap=cv2.VideoCapture('http://admin:admin@192.168.1.103:8081')
i=1
while True:
    print(i)
    i+=1
    ret,frame=cap.read()
    if not ret or cv2.waitKey(1)==ord('q'):
        break
    else:
        frame=tracker.track(frame)
        cv2.imshow('track',frame)
cap.release()
cv2.destroyAllWindows()