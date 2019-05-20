import cv2
import numpy as np
import os
import time
import mailing
import routine
import board

from PIL import Image
from logger import log

class Recognizer:
    def __init__(self):
        self.labels = ['Alex Galea', 'Alexandra Girda', 'Michelle Bettendorf', 'Alex Mihaescu', 'Bogdan Pocol', 'Ionut Putanu', 'Sorin Rista']
        self.allowed = ['Alex Mihaescu']

        log('Face detector initializing ...')
        self.face_cascade = cv2.CascadeClassifier('classifier_data.xml')
        log('Face detector initialized.')

        log('Creating face recognizer ...')
        self.recognizer = cv2.face.LBPHFaceRecognizer_create() # face recognizer
        log('Face recognizer created.')
        log('Loading trained model ...')
        self.recognizer.read("trained_model.yml") # load the trained data
        log('Trained model loaded.')

        log('Initializing capture device ...')
        self.cap = cv2.VideoCapture(0) #Get vidoe feed from the Camera
        log('Capture device initialized.')

        log('Testing capture device ...')
        cameraWorks, testImage = self.cap.read()
        if cameraWorks:
            log('Capture device is working.')
        else:
            log('Capture device is not working ...')

        self.delta = 0.5
        self.saw_faces = {}
        self.starting_time = time.time() #starting timestamp
        log('Staring time is %f' % self.starting_time)

        for name in self.labels:
            self.saw_faces[name] = [0, self.starting_time] # keeping count of the faces detected [count, last_time_seen]
        log('Mailing service initializing ...')
        self.mailer = mailing.sPiMailing('Alex Mihaescu', 'mihaescuac@gmail.com')
        log('Mailing service initialized.')
        routine.init()
        routine.setDnd()
        log('Recognizer initialized.')

    def recognize(self):
        while True:
            ret, img = self.cap.read() # take a frame
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
                        if time_st - self.saw_faces[name][1] < self.delta:
                            self.saw_faces[name][0] = self.saw_faces[name][0]+1
                        else:
                            self.saw_faces[name][0] = 0

                        self.saw_faces[name][1] = time_st

                        if self.saw_faces[name][0] > 10: # if a person is recognized
                            log('Recognized ' + name)
                            if name in self.allowed:
                                board.unlock()
                                print('Do something when recognized an allowed')
                            elif routine.away():
                                cv2.imwrite('intruder.jpg', img)
                                if routine.doNotDisturb:
                                    self.mailer.notifyWhileInDnd()
                                    self.kill()
                                    break
                                else:
                                    self.mailer.notifyWhileAway()   
                            else:
                                print('Do something when other than allowed')
                            
                    
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

                cv2.imshow('Preview',img) #Display the Video
                if cv2.waitKey(20) & 0xFF == ord('q'): #EXIT
                    log('Kill message was recieved')
                    self.mailer.kill()
                    self.kill()
                    return
            else:
                log ('ERROR Capture failed') # if loading a frame failed (camera not working)
                self.kill()
                break

    def restart(self):
        log('Recognized allowed face. Unlocking. Restarting...')
        self.__init__()

    def kill(self):
         # When everything done, release the capture
        self.cap.release()
        cv2.destroyAllWindows()
        board.kill()
        log('Recognizer is shut down ...')