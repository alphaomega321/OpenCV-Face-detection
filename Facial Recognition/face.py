import numpy as np
import cv2
import pickle
import os

face_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create() 
recognizer.read("trainer.yml") #Reading the trained data

#Read the label->id mapping but we need reverse i.e  id->lable
lables = {}
with open("labels.pickle", 'rb') as f:
	og_labels = pickle.load(f)
	lables = {v:k for k,v in og_labels.items()}


while True:

	ret, frame = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
	if(len(faces)==0):
		beep = lambda x: os.system("echo -n '\a': sleep 0.2:" * x)
		beep(3)


	else:
		for (x,y,w,h) in faces:
			roi = frame[y:y+h, x:x+h]
			roi_gray = gray[y:y+h, x:x+h]
			cv2.imshow('face',roi)
			cv2.imwrite('temp.png',roi)


			#Predict
			id_, conf = recognizer.predict(roi_gray) 

			if conf>=45:
				font = cv2.FONT_HERSHEY_SIMPLEX
				name = lables[id_]
				font_size = 1
				font_color = (255,255,255)
				stroke = 2
				cv2.putText(frame, name, (x,y), font, font_size, font_color, stroke, cv2.LINE_AA)

				
			#Creating a rectangle around the face
			color = (255,0,0) #BGR hence color blue
			stroke = 2 #Width of rectangle

			end_cord_x = x+w
			end_cord_y = y+h

			cv2.rectangle(frame, (x,y), (end_cord_x,end_cord_y), color, stroke)

		cv2.imshow('frame',frame)
		if cv2.waitKey(20) & 0xFF == ord('q'):
			break


cap.release()
cv2.destroyAllWindows()
