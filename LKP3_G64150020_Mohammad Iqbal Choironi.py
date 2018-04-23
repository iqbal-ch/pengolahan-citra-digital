import cv2
import  numpy as np
from matplotlib import pyplot as plt

#fungsi untuk gray scale
def grayscale(data):
	row,col,ch = data.shape
	graykanvas = np.zeros((row,col,1),np.uint8)
	for i in range(row):
		for j in range(col):
			gray = 0.299* data[i,j,0]  + 0.587 * data[i,j,1] + 0.114 * data[i,j,2]
			graykanvas.itemset((i, j, 0), gray)
	
	return graykanvas

#fungsi contrast stretch
def stretch(data):
	row, col, ch = data.shape
	output = np.zeros((row, col, 1), np.uint8)
	min = max = data[0, 0]
	for i in range (0, row):
		for j in range (0, col):
			if data[i, j] < min:
				min = data[i,j]
			if data[i, j] > max:
				max = data[i, j]

	bawah = max - min

	for i in range (0, row):
		for j in range (0, col):
			normalize = (float(data[i, j] - min) / bawah) * 255
			output.itemset((i, j, 0), normalize)

	return output

#fungsi untuk histogram equalization
def equalization(data):	
	row, col, ch = data.shape
	canvas = np.zeros((row,col,1), np.uint8)
	
	#menghitung kemunculan tiap pixel
	pixel=[0]*256
	for i in range(0, row):
		for j in range(0, col):
			nilai = int(data[i,j])
			pixel[nilai] = pixel[nilai] + 1
			
	#menghitung peluang nilai kemunculan tiap pixel
	for i in range(0, 256):
		pixel[i] = float(pixel[i])/float(row*col)
		
	#menghitung histogram kumulatif
	for i in range(0, 256):
		pixel[i] = pixel[i]+pixel[i-1]
		
	#menghitung equalized histogram
	for i in range(0,256):
		pixel[i]=pixel[i]*(256-1)
		
	#memasukkan ke dalam kanvas
	for i in range(0, row):
		for j in range(0, col):
			nilai = int(data[i,j])
			nilai = pixel[nilai]
			canvas.itemset((i,j,0),nilai)

	return canvas

data = cv2.imread('car.png')
gray = grayscale(data)
cs = stretch(gray)
hq = equalization(gray)

cv2.imshow("original", data)
cv2.imshow("grayscale", gray)
cv2.imshow("contrast steaching", cs)
cv2.imshow("equalized", hq)

#histrogram gray scale
hisgray = cv2.calcHist([gray],[0], None, [256], [0,256])
plt.hist(gray.ravel(), 255, [0,256], label="Gray")
plt.title("Histogram Grayscale")
plt.show()

#histrogram contrash streacing
hiscs = cv2.calcHist([cs],[0], None, [256], [0,256])
plt.hist(cs.ravel(), 255, [0,256], label="Contras Streching")
plt.title("Contras Streching")
plt.show()

#histrogram rataan histogram
hishq = cv2.calcHist([hq],[0], None, [256], [0,256])
plt.hist(hq.ravel(), 255, [0,256], label="Histogram Equalization")
plt.title("Histogram Equalization")
plt.show()

cv2.waitKey(0)



