import numpy as np
import cv2

#Taking input from default camera
cap = cv2.VideoCapture(0)

while True:

	#Capture frame by frame
	ret, frame = cap.read()

	#Convert frame to greyscale
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


	#Display the output

	cv2.imshow('frame',frame)
	cv2.imshow('gray',gray)

	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

#Destroy the object
cap.release()
cv2.destroyAllWindows()
