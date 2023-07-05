import cv2 as cv

img= cv.imread('../Photos/cat1.jpeg')
cv.imshow('Cat', img)

#Averaging
average =cv.blur(img, (3,3))
cv.imshow('average blur',average)

#GAUSSIAN BLUR
gauss =cv.GaussianBlur(img, (3,3),0)
cv.imshow("gausian",gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('median', median)

# BILATERAL
bilateral = cv.bilateralFilter(img,5,15,15)
cv.imshow('bilateral' , bilateral)

cv.waitKey(0)