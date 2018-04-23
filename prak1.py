import numpy as np
import cv2

img = cv2.imread('Sampang.png',0)	#untuk grey scale
img2 = cv2.imread('Sampang.png',1)	#untuk rgb

print('img')
print(img[0,0])	#untuk nge prin nilai grayscale di arr 0,0 

cv2.imshow('nama file yang akan di simpan',img)

cv2.waitKey(0)
