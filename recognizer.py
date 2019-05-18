#Program to Detect the Face and Recognise the Person based on the data from face-trainner.yml

import cv2 #For Image processing 
import numpy as np #For converting Images to Numerical array 
import os #To handle directories 
import time
from PIL import Image #Pillow lib for handling images

labels = ['Alex Galea', 'Alexandra Girda', 'Michelle Bettendorf', 'Alex Mihaescu', 'Bogdan Pocol', 'Ionut Putanu', 'Sorin Rista'] 
# Haar cascade classifier to detect faces in an image
face_cascade = cv2.CascadeClassifier('classifier_data.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create() # face recognizer

recognizer.read("trained_model.yml") # load the trained data

delta = 0.2

cap = cv2.VideoCapture(0) #Get vidoe feed from the Camera

starting_time = time.time() #starting timestamp
saw_faces = {}
for name in labels:
    saw_faces[name] = [0, starting_time] # keeping count of the faces detected [count, last_time_seen]

while(True):
    ret, img = cap.read() # Break video into frames
    if ret:
        gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert Video frame to Greyscale
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5) #Recog. faces
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w] #Convert Face to greyscale 

            id_, conf = recognizer.predict(roi_gray) #recognize the Face
        
            if conf >= 80:                
                font = cv2.FONT_HERSHEY_SIMPLEX #Font style for the name 
                name = labels[id_] #Get the name from the List using ID number 
                cv2.putText(img, '%s %.2f' % (name, conf), (x,y), font, 1, (0,0,255), 2)
                time_st = time.time()
                print(time_st - saw_faces[name][1])
                if time_st - saw_faces[name][1] < delta:
                    saw_faces[name][0] = saw_faces[name][0]+1
                else:
                    saw_faces[name][0] = 0

                saw_faces[name][1] = time_st

                if saw_faces[name][0] > 10:
                    print('Recognized ' + name)
            
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.imshow('Preview',img) #Display the Video
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        print ('Nope') # if loading a frame failed

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
