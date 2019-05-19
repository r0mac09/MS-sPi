#Program to Detect the Face and Recognise the Person based on the data from face-trainner.yml

import cv2 #For Image processing 
import numpy as np #For converting Images to Numerical array 
import os #To handle directories 
import time
import mailing
import board
from PIL import Image #Pillow lib for handling images
from logger import log
class Recognizer:
    def __init__(self):
        self.labels = ['Alex Galea', 'Alexandra Girda', 'Michelle Bettendorf', 'Alex Mihaescu', 'Bogdan Pocol', 'Ionut Putanu', 'Sorin Rista']
        self.allowed = ['Alex Mihaescu']
        # Haar cascade classifier to detect faces in an image
        self.face_cascade = cv2.CascadeClassifier('classifier_data.xml')
        log('Face dedtection initialized ...')
        self.recognizer = cv2.face.LBPHFaceRecognizer_create() # face recognizer
        self.recognizer.read("trained_model.yml") # load the trained data
        log('Face recognizer innitialized ...')
        self.delta = 0.5 # max time delta between face recognition
        self.cap = cv2.VideoCapture(0) #Get vidoe feed from the Camera
        cameraWorks, testImage = self.cap.read()
        if cameraWorks:
            log('Camera is working ...')
        else:
            log('ERROR Camera is not working ...')

        self.starting_time = time.time() #starting timestamp
        self.saw_faces = {}
        for name in self.labels:
            self.saw_faces[name] = [0, self.starting_time] # keeping count of the faces detected [count, last_time_seen]
        self.mailer = mailing.sPiMailing('Alex Mihaescu', 'mihaescuac@gmail.com')
        log('Mailer initialized ...')
    
    def start(self):
        try:
            while(True):
                ret, img = self.cap.read() # Break video into frames
                if ret:
                    gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert Video frame to Greyscale
                    faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5) #Recog. faces
                    for (x, y, w, h) in faces:
                        roi_gray = gray[y:y+h, x:x+w] #Convert Face to greyscale 

                        id_, conf = self.recognizer.predict(roi_gray) #recognize the Face
                    
                        if conf >= 80:                
                            font = cv2.FONT_HERSHEY_SIMPLEX #Font style for the name 
                            name = self.labels[id_] #Get the name from the List using ID number 
                            cv2.putText(img, '%s %.2f' % (name, conf), (x,y), font, 1, (0,0,255), 2)
                            time_st = time.time()
                            log(time_st - self.saw_faces[name][1])
                            if time_st - self.saw_faces[name][1] < self.delta:
                                self.saw_faces[name][0] = self.saw_faces[name][0]+1
                            else:
                                self.saw_faces[name][0] = 0

                            self.saw_faces[name][1] = time_st

                            if self.saw_faces[name][0] > 10: # if a person is recognized
                                log('Recognized ' + name)
                                if name in self.allowed:
                                    return True
                                else:
                                    return False
                                
                        
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

                    cv2.imshow('Preview',img) #Display the Video
                    if cv2.waitKey(20) & 0xFF == ord('q'):
                        board.kill()
                        self.kill()
                        return None
                else:
                    log ('Nope') # if loading a frame failed (camera not working)
        except KeyboardInterrupt:
            self.kill()

    def kill(self):
         # When everything done, release the capture
        self.cap.release()
        cv2.destroyAllWindows()

