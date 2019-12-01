import numpy as np
import cv2

cap = cv2.VideoCapture(0)

def setRes(w,h): #Set the resolution
	cap.set(3,w)
	cap.set(4,h)


setRes(6400,4800)
while True:

	ret, frame = cap.read()
	cv2.imshow('frame',frame)

	if cv2.waitKey(20) & 0xFF==ord('q'):
		break


cap.release()
cv2.destroyAllWindows()