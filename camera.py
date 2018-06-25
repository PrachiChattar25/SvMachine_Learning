#!/usr/bin/python3

import cv2
import random 
 
#now starting the camera

cap=cv2.VideoCapture(0)

while cap.isOpened():
	print ("Camera is working\n:-) Muskurana bnta h ")
	status,frame=cap.read()
	bwimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.rectangle(frame,(100,100),(200,200),(255,0,0),2)
	font=cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(frame,'Free_time',(100,100),font,2,(0,0,255),cv2.LINE_AA)
	cv2.imshow("camera1",frame)
	x=random.random()
	y=str(x)[2:6]
	cv2.imwrite('adhoc'+y+'.jpg',frame)
	cv2.imshow("camera2",bwimg)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()
cap.release()
		
