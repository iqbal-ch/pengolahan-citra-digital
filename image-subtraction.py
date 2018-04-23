import cv2
import numpy as np 

data = cv2.imread('whitefly.png')
row,col,ch = data.shape

normalRGB = np.zeros((row,col,ch),np.uint8)
hasil = np.zeros((row,col,ch),np.uint8)

#normalisasi rgb dulu nih....
for i in range(row):
    for j in range(col):
        for z in range(ch):
            normalRGB[i,j,z] = data[i,j,z] / (data[i,j,0] + data[i,j,1] + data[i,j,2])

#pengurangan (subtraction)
for i in range(row):
    for j in range(col):
        for z in range(ch):
            hasil[i,j,z] = abs(normalRGB[i,j,z] - data[i,j,z])

# for i in range(row):
#  	for j in range(col):
#  		if graykanvas[i,j]>150:
#  			binarykanvas[i,j] = 225
#  		else:
#  			binarykanvas[i,j] = 0

cv2.imshow('hasil',hasil)
cv2.imshow('asli',data)

cv2.waitKey()
cv2.destroyAllWindows() 

