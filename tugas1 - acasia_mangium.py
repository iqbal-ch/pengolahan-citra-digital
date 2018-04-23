import numpy as np
import cv2

#Ukuran Image
image = cv2.imread("acasia_mangium.png")
row,col,ch = image.shape
print("row = " +str(row)+ "; col = "+str(col))

cv2.imshow('Original', image)

imgGray = np.zeros((row,col,1), np.uint8)
threshold = np.zeros((row,col,1), np.uint8)


for i in range(0,row):
    for j in range(0,col):
        blue, green, red = image[i,j]

        #Grayscale
        Gray = (red * 0.299 + green * 0.587 + blue * 0.114)
        imgGray.itemset((i,j,0),Gray)

        #Threshold

        grays = imgGray[i,j]

        if(grays < 180):
            threshold.itemset((i,j,0), 0)
        else:
            threshold.itemset((i,j,0), 255)

cv2.imshow('Acasia Mangium', threshold)
cv2.imwrite('acasia_mangium_penyakit.png', threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()
