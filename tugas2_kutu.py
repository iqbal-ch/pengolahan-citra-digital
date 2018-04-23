import cv2
import numpy as np 

data = cv2.imread('whitefly.png')
row,col,ch = data.shape

normalRGB = np.zeros((row,col,ch),np.uint8)
pengurangan = np.zeros((row,col,ch),np.uint8)
graykanvas = np.zeros((row,col,1),np.uint8)
hasil = np.zeros((row,col,1),np.uint8)


#normalisasi rgb dulu nih....
for i in range(row):
    for j in range(col):
        for z in range(ch):
            normalRGB[i,j,z] = data[i,j,z] / (data[i,j,0] + data[i,j,1] + data[i,j,2])

#pengurangan (subtraction)
for i in range(row):
    for j in range(col):
        for z in range(ch):
            pengurangan[i,j,z] = abs(normalRGB[i,j,z] - data[i,j,z])

#jadi grayscale 
for i in range(row):
	for j in range(col):
		graykanvas[i,j] = 0.299 * pengurangan[i,j,0]  + 0.587 * pengurangan[i,j,1] + 0.114 * pengurangan[i,j,2]

for i in range(row):
 	for j in range(col):
 		if graykanvas[i,j]>100:
 			hasil[i,j] = 0
 		else:
 			hasil[i,j] = 225

cv2.imshow('hasil',hasil)
cv2.imshow('asli',data)

cv2.waitKey()
cv2.destroyAllWindows() 

