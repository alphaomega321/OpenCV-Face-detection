import os
import cv2
import numpy as np
import pickle
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #/home/saransh/Facial Recognition
image_dir = os.path.join(BASE_DIR,"images") #/home/saransh/Facial Recognition/images

face_cascade = cv2.CascadeClassifier('data/haarcascades/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create() #LBPH recognizer is good for training


#root: /home/saransh/Facial Recognition/images/(Amey,Vaibha,Saransh etc)
#files: ['div7.png', 'saransh2.png', 'Amey4.png', 'div1.png', 'pranau7.png', 'div3.png', 'saransh7.png', 'vaibhav7.png', 'Amey1.png', 'mayank7.png', 'pranau2.png', 'vaibhav6.png', 'vaibhav5.png', 'saransh3.png', 'div4.png', 'vaibhav2.png', 'mayank8.png', 'vaibhav3.png', 'Vaibhav1.png', 'Vineet1.png', 'div2.png', 'vineet2.png', 'mayank4.png', 'div6.png', 'pranau4.png', 'div5.png', 'mayank9.png', 'Vineet5.png', 'pranau5.png', 'Amey2.png', 'saransh5.png', 'saransh1.png', 'Vineet3.png', 'Vineet4.png', 'Amey5.png', 'saransh4.png', 'Mayank3.png', 'pranau6.png', 'saransh6.png', 'mayank2.png', 'Mayank1.png', 'pranau3.png', 'Amey3.png', 'vaibhav4.png', 'mayank3.png', 'Amey6.png', 'pranau1.png', 'mayank5.png']
#path:  /home/saransh/Facial Recognition/images/Amey/1.jpg ....

y_labels = []
x_train = []
label_ids = {} #Mapping of lables to id: Amey->0 Mayank->1 etc
curr_id = 0


for root, dirs, files in os.walk(image_dir):
	for file in files:
		if file.endswith("png") or file.endswith("jpg"):
			path = os.path.join(root,file)
			label = os.path.basename(root).replace(" ",'-').lower()
			
			#We need label as some number
			#We need pictures(pil_image) in numpy array and gray form

			pil_image = Image.open(path).convert('L') #Convert path to image, covert(L) coverts image to GRAY
			size = (550,550)
			final_image = pil_image.resize(size, Image.ANTIALIAS) #Resize
			image_array = np.array(final_image, "uint8") #Convert image to numpy array
			
			if not label in label_ids: 
				label_ids[label] = curr_id
				curr_id += 1

			id_ = label_ids[label]

			faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)
			for (x,y,w,h) in faces:
				roi = image_array[y:y+h, x:x+w]
				x_train.append(roi)
				y_labels.append(id_)

'''print(x_train)
print(y_labels)
print(label_ids)'''

print(label_ids)
print(y_labels)

#We need to save lables so that we can use them inside face.py we use pickle library for the same

with open("labels.pickle", 'wb') as f:
	pickle.dump(label_ids, f)

recognizer.train(x_train, np.array(y_labels))
recognizer.write("trainer.yml") #Save the training data

