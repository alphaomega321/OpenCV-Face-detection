import numpy as np
import cv2
import os

face_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture(0)


#Read the label->id mapping but we need reverse i.e  id->lable
Reg_no = str(input())
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR,"images")
folder_dir = os.path.join(image_dir,Reg_no)
print(folder_dir)
snaps = 0

while True:

	ret, frame = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

	for (x,y,w,h) in faces:
		roi = frame[y:y+h, x:x+h]
		roi_gray = gray[y:y+h, x:x+h]
		cv2.imshow('face',roi)
		
		snaps += 1
		cv2.imwrite(folder_dir+'/'+str(snaps)+'.png',frame)

		#Creating a rectangle around the face
		color = (255,0,0) #BGR hence color blue
		stroke = 2 #Width of rectangle

		end_cord_x = x+w
		end_cord_y = y+h

		cv2.rectangle(frame, (x,y), (end_cord_x,end_cord_y), color, stroke)

	cv2.imshow('frame',frame)
	if cv2.waitKey(100) & 0xFF == ord('q'):
		break

	elif snaps>100:
		break


cap.release()
cv2.destroyAllWindows()
