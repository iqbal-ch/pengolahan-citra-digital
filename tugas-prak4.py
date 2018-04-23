import numpy as np
from matplotlib import pyplot as plt
import cv2


#Grayscale
def grayscale(img):
	row, col, ch = img.shape
	graykanvas = np.zeros((row, col, 1), np.uint8)
	binerkanvas = np.zeros((row, col, 1), np.uint8)
	truncatekanvas = np.zeros((row, col, 1), np.uint8)
	for i in range(0, row):
		for j in range(0, col):
			blue, green, red = img[i, j]
			gray = red * 0.299 + green * 0.587 + blue * 0.114
			graykanvas.itemset((i, j, 0), gray)

	return graykanvas

#fungsi contrast stretch
def stretch(img):
	row, col, raw =img.shape
	output = np.zeros((row, col, 1), np.uint8)
	min = max = img[0, 0]
	for i in range (0, row):
		for j in range (0, col):
			if img[i, j] < min:
				min = img[i, j]
			if img[i, j] > max:
				max = img[i, j]

	bawah = max - min
	for i in range (0, row):
		for j in range (0, col):
			normalize = (float(img[i, j] - min) / bawah) * 255
			output.itemset((i, j, 0), normalize)
	return output

#Histogram
def histogray(img):
	buckets = [0] * 300
	arraynorm = [0] * 300
	scale = 1
	histocol = 255
	historow = 150
	border = 30
	canvashisto = np.zeros(((historow+border), histocol, 1), np.uint8)
	row, col, raw = img.shape
	graykanvas = np.zeros9((row, col, 1), np.uint8)
	for i in range (0, row):
		for j in range (0, col):
			buckets[int(img[i, j])] += 1
	maks = max(buckets)
	mins = min(buckets)
	for intent in range (0, 255):
		jumlahperbar = buckets[intent]
		normal = int(float(jumlahperbar) / float(maks) * float (historow))
		arraynorm[intent] = normal
		for y in range (int(historow-normal+border), historow+border):
			canvashisto.itemset((y, intent, 0), 255)
	return canvashisto

gambar = cv2.imread('car.png')
gray = grayscale(gambar)

#cntrast streching
contrast = stretch(gray)
histStrech = cv2.calcHist([contrast], [0], None, [256], [0,256])

#equalize
equ = cv2.equalizeHist(gray)
histEqu = cv2.calcHist([equ], [0], None, [256], [0,256])

cv2.imshow("Equalized", equ)
cv2.imshow("Contrast Strech", contrast)
cv2.imshow("Real Pict", gray)

#histogram ori
histGray = cv2.calcHist([gambar], [0], None, [256], [0,256])
plt.hist(gambar.ravel(), 256, [0,256], label = "Ori")
plt.title("Histogram Ori")
plt.show()

#histogram strecth
histCont = cv2.calcHist([contrast], [0], None, [256], [0,256])
plt.hist(contrast.ravel(), 256, [0,256], label = "Contrast")
plt.title("Histogram Contrast")
plt.show()

#histogram gray
histEqua = cv2.calcHist([equ], [0], None, [256], [0,256])
plt.hist(equ.ravel(), 256, [0,256], label = "Equalize")
plt.title("Histogram Equalize")
plt.show()

cv2.waitKey(0)