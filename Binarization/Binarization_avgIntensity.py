import cv2
import numpy as np
from matplotlib import pyplot as plt

I = cv2.imread('hwf.jpeg')
cv2.namedWindow('hwf',cv2.WINDOW_AUTOSIZE)
cv2.imshow('',I)
cv2.waitKey(0)
r, c, cl = I.shape
Sum = 0

for i in range(r):
	for j in range(c):
		Sum += ((I[i,j,1]+I[i,j,2]+I[i,j,0])**2)
#Finding mean of all pixel intensities and setting it as the threshold
T_avg = np.log(((Sum)/(r*c*cl))**0.5)

for i in range(r):
	for j in range(c):
		if ((I[i,j,1]+I[i,j,2]+I[i,j,0])>T_avg):
			I[i,j] = 0
		else:
			I[i,j] = 255
cv2.namedWindow('hw0',cv2.WINDOW_AUTOSIZE)
cv2.imshow('',I)
cv2.waitKey(0)
			
