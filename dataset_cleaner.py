#Program to train with the faces and create a YAML file

import cv2 #For Image processing 
import numpy as np #For converting Images to Numerical array 
import os #To handle directories 
from PIL import Image #Pillow lib for handling images 

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
# recognizer = cv2.createLBPHFaceRecognizer()

pev_person_name = ""
y_ID = []
x_train = []

dataset = os.path.join(os.getcwd(), "dataset") #Tell the program where we have saved the face images 
print (dataset)

#counters
useless_pictures = 0
useful_pictures = 0
pictures = 0


for root, dirs, files in os.walk(dataset): #go to the face image directory 
	for file in files: #check every directory in it 
		if file.endswith("jpeg") or file.endswith("jpg") or file.endswith("png"): #for image files ending with jpeg,jpg or png 
			pictures = pictures+1
			path = os.path.join(root, file)
			person_name = os.path.basename(root)
			
			print('checking ' + path)

			Gery_Image = Image.open(path).convert("L") # convert the image to greysclae using Pillow
			Crop_Image = Gery_Image.resize( (512,512) , Image.ANTIALIAS) #Crop the Grey Image to 550*550 (Make sure your face is in the center in all image)
			Final_Image = np.array(Crop_Image, "uint8")
			faces = face_cascade.detectMultiScale(Final_Image, scaleFactor=1.05, minNeighbors=5) #Detect The face in all sample image 
			if(str(faces) == '()'): #if no face detected in the image
				useless_pictures = useless_pictures+1
				os.remove(path)
				print('deleted ' + file)
				continue
			useful_pictures = useful_pictures+1

print('%d useless, %d useful, %d total' % (useless_pictures, useful_pictures, pictures))
