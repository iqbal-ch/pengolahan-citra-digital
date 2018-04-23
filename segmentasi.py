import cv2
import numpy as np 

data = cv2.imread('acasia.png')
row,col,ch = data.shape

normalRGB = np.zeros((row,col,ch),np.uint8)
pengurangan = np.zeros((row,col,ch),np.uint8)
graykanvas = np.zeros((row,col,1),np.uint8)
hasil = np.zeros((row,col,1),np.uint8)


#jadi grayscale 
for i in range(row):
	for j in range(col):
		graykanvas[i,j] = 0.299 * data[i,j,0]  + 0.587 *data[i,j,1] + 0.114 * data[i,j,2]

for i in range(row):
 	for j in range(col):
 		if graykanvas[i,j]>177:
 			hasil[i,j] = 0
 		else:
 			hasil[i,j] = 225

cv2.imshow('hasil',hasil)
cv2.imshow('asli',data)

cv2.waitKey()
cv2.destroyAllWindows() 

