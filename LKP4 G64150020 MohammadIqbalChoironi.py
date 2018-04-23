import cv2
import numpy as np 

img = cv2.imread('koinIPB.jpg',0)
high = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
low = np.array([[-1,-1,-1],[-1,1,-1],[-1,-1,-1]])

cv2.imshow("original image", img)

def convolution(img, msk):
    row, col = img.shape
    kanvashasil = np.zeros((row,col,1),np.uint8)
    rm, rc = msk.shape
    for i in range(0, row):
        for j in range(0, col):
            imageSum = maskSum = 0
            for a in range(int(rm/2), int(rm-rm/2)):
                for b in range(int(rc/2), int(rc-rc/2)):
                    if((i+a)>=0 and (j+b)>=0 and i+a<row and j+b<col):
                        imageSum += img[i+a, j+b] * msk[a+int(rm)/2, b+int(rc)/2]
                        maskSum += msk[a+int(rm)/2, b+int(rc)/2]
            if maskSum == 0:
                intensity = imageSum
            else:
                intensity = int(imageSum/maskSum)
            if intensity > 255:
                intensity = 255
            elif intensity < 0:
                intensity = 0
            kanvashasil.itemset((i, j, 0), intensity)
    return kanvashasil

resulthigh = convolution(img, high)
cv2.imshow("convolution highpass", resulthigh)

resultlow = convolution(img, low)
cv2.imshow("convolution lowpass", resultlow)

cv2.waitKey(0)
cv2.destroyAllWindows()
