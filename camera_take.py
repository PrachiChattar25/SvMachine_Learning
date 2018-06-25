#!/usr/bin/python3
#Camera Demo
import cv2
import cgi

#To start web camera or external web camera
capture=cv2.VideoCapture(0) 
'''0 used for the laptop camera
1 used for the the External Camera and similarly for 2,3.. '''

if capture.isOpened() :
	print("Camera is ready to take picture\n:-) Smile Please")

#It tells camera to take data and here we need to give time till when it should take data
#Gives current camera data, after frame take camera status
	status,frame=capture.read()
	cv2.imshow("Frame1",frame)
	cv2.waitKey(0)
	capture.release()
else :
	print("Check your camera drivers with OS")
	
