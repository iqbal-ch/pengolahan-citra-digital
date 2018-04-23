import cv2
import numpy as np 

data = cv2.imread('acasia.png')
row,col,ch = data.shape

negativekanvas = np.zeros((row,col,ch),np.uint8)

for i in range(row):
    for j in range(col):
        for z in range(ch):
		    negativekanvas[i,j,z] = 255 - data[i,j,z]

cv2.imwrite('negative.jpg',negativekanvas)
cv2.imshow('hasil',negativekanvas)

cv2.waitKey()
cv2.destroyAllWindows() 

