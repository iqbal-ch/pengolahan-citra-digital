import cv2
import numpy as np

img = cv2.imread('beri.jpg')
lena = cv2.imread('lena-noise.png')

blur = cv2.blur(img, (7,7))
# gausblur = cv2.GaussianBlur(img,(5,5),0)
# median = cv2.medianBlur(lena,5)
# bilablur = cv2.bilateralFilter(imgn9,75,75)

kernel = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
#kernel = np.ones((3,3),np.float32)
dst = cv2.filter2D(img,-1,kernel)
print(kernel)

cv2.imshow("ori", img)
cv2.imshow("blur", blur)
#cv2.imshow("gaus", gausblur)
cv2.imshow("filter2d", dst)
#cv2.imshow("med", median)
#cv2.imshow("bilateral", bilablur)

cv2.waitKey(0)
cv2.destroyAllWindows()
