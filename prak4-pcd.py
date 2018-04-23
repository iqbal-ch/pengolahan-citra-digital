import cv2
import  numpy as np
from matplotlib import pyplot as plt

data = cv2.imread('a.png')

gray = cv2.cvtColor(data,cv2.COLOR_BGR2GRAY)
cv2.imshow("lol",gray)


#histrogram gray scale
hisgray = cv2.calcHist([gray],[0], None, [256], [0,256])
plt.hist(gray.ravel(), 255, [0,256], label="Gray")
plt.title("Histogram Grayscale")
plt.show()

#histogram BGR

color = ('b','g','r')
for i, col in enumerate(color):
	hisrgb = cv2.calcHist([data], [i], None, [256], [0,256])
	plt.plot(hisrgb, color = col)
	plt.xlim([0,256])

plt.title("Histogram BGR")
plt.show()

#contras streaching

cv2.keyWait(0)
cv2.destroyAllWindows()
