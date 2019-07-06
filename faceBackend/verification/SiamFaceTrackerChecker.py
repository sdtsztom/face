import faceBackend as fb
import cv2

tracker=fb.SiamFaceTracker([1])
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    if not ret or cv2.waitKey(1)==ord('q'):
        break
    else:
        frame=tracker.track(frame)
        cv2.imshow('track',frame)
cap.release()
cv2.destroyAllWindows()