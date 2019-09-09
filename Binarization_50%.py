import cv2
import numpy as np
from matplotlib import pyplot as plt

#read image in greyscale for thresholding
I = cv2.imread('hwf.jpeg',0)
cv2.namedWindow('hw02',cv2.WINDOW_AUTOSIZE)
cv2.imshow('Original',I)
cv2.waitKey(0)
r, c= I.shape
Sum = 0

#Calculate the histogram as
hist = np.zeros(I.shape)
hist = cv2.calcHist([I], [0], None, [256], [0, 256])
print (np.max(hist))

#normalize the histogram
cv2.normalize(hist, hist)
print (hist.shape)
#plt.plot(hist)

#calculate half area unde the histogram
total_area = np.sum(hist[0:256])
half_area = total_area/2

flag = 1
#Calculate a threshold based on 50% of the area
for i in range(256):
# 	area = np.sum(hist[0:i])
# 	if (np.abs(area-half_area)<100000):
# 		T = i
# 	else:
	a1 = np.sum(hist[0:i])
	a2 = np.sum(hist[i:256])
	if (np.abs(a2-a1)<0.02) and flag==1:
		T = i
		flag = 0

print (T)
						
#Applying the threshold to the image to binarize
for i in range(r):
	for j in range(c):
		if ((I[i,j])>T):
			I[i,j] = 255
		else:
			I[i,j] = 0


cv2.namedWindow('hw02',cv2.WINDOW_AUTOSIZE)
cv2.imshow('',I)
cv2.waitKey(0)
			