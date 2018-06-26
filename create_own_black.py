#!/usr/bin/python3
import numpy as np
import cv2

img=np.zeros((300,300))
img1=np.ones((300,300))

cv2.imshow('Black',img)
cv2.imshow('White',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
