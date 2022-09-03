import cv2
import numpy as np
import os
#from distutils.log import Log
import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import ttk
import customtkinter as ctk
from tkinter import Canvas, Text

from setuptools import Command

class recognise:
    def login():
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(r'training.yml')
        faceCascade = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")

        font = cv2.FONT_HERSHEY_SIMPLEX

        #iniciate id counter
        id = 0

        # names related to ids
        names = ['None', 'Maryam', 'Tufail', "Ammar"] 

        # Initialize and start realtime video capture
        print("\n \n \nPlace your face near camera :)")
        cam = cv2.VideoCapture(0)
        cam.set(3, 640) # set video widht
        cam.set(4, 480) # set video height

        # Define min window size to be recognized as a face
        minW = 0.1*cam.get(3)
        minH = 0.1*cam.get(4)

        while True:

            ret, img =cam.read()              #ret returns boolean value

            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale( gray,scaleFactor = 1.2,minNeighbors = 5,minSize = (int(minW), int(minH)),)

            for(x,y,w,h) in faces:

                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

                id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
                # Check if confidence is less then 100 ==> "0" is perfect match 
                if (confidence < 70):
                    id = names[id]
                    confidence_1 = "  {0}%".format(round(100 - confidence))
                    
                else:
                    id = "unknown"
                    confidence_1 = "  {0}%".format(round(100 - confidence))
                
                cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
                cv2.putText(img, str(confidence_1), (x+5,y+h-5), font, 1, (255,255,0), 1)  
            
            cv2.imshow('camera',img) 

            k = cv2.waitKey(10) & 0xff   #enter to exit
            if k == 13:
                break
        if int(confidence)<70 :
            print("\nYou have logged in sucessfully")
        else:
            print("\nFailed to login")
            exit()
        cam.release()
        cv2.destroyAllWindows()