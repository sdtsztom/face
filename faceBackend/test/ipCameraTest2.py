import urllib.request
import cv2
import numpy as np

# Replace the URL with your own IPwebcam shot.jpg IP:port
url='http://192.168.1.100:8080/shot.jpg'

while True:

# Use urllib to get the image from the IP camera
	imgResponse = urllib.request.urlopen(url)
 
 # Numpy to convert into a array
	imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
 
 # Decode the array to OpenCV usable format
	img = cv2.imdecode(imgNp,-1)
 
 
 # put the image on screen
	cv2.imshow('IPWebcam',img)

# Program closes if q is pressed
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break