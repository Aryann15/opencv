import cv2 as cv
import numpy as np

img = cv.imread('../Photos/cat1.jpeg')
cv.imshow('cat',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Laplacion
lap = cv.Laplacian(gray,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacion',lap)

#Sobel

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx,sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y',sobely)
cv.imshow('combined Sobel', combined_sobel)

cv.waitKey(0)