import cv2
import numpy as np
from matplotlib import pyplot as plt

I = cv2.imread('hw0.jpeg')
cv2.namedWindow('hw0',cv2.WINDOW_AUTOSIZE)
cv2.imshow('',I)
cv2.waitKey(0)
r, c, cl = I.shape
Sum = 0

for i in range(r):
	for j in range(c):
		if i%2 != 0 and j%2 ==0:
			I[i,j] = 255
		else:
			I[i,j] = 0


cv2.namedWindow('hw0',cv2.WINDOW_AUTOSIZE)
cv2.imshow('',I)
cv2.waitKey(0)
			