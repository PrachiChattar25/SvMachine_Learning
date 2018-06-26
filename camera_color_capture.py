#!/usr/bin/python3

import cv2,time

#reading image

cap=cv2.VideoCapture(0)

while cap.isOpened():

	#taking frames
	status,frame=cap.read()
	#extracting only red color
	#onlyred=cv2.inRange(frame,(0,0,0),(30,30,255))
	#extracting only green color
	#onlygreen=cv2.inRange(frame,(0,0,0),(30,255,30))
	#extracting only blue color
	onlyblue=cv2.inRange(frame,(50,10,10),(255,30,30))
	
	#cv2.imshow('onlyred',onlyred)
	#cv2.imshow('onlygreen',onlygreen)
	cv2.imshow('onlyblue',onlyblue)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()
