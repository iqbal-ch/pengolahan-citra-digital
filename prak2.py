import cv2
import numpy as np 

data = cv2.imread('Lenna.png')
gray = cv2.cvtColor(data,cv2_COLOR_BGR2GRAY)

graykanvas = np.zeroes((row,col,1),np.uint8)

