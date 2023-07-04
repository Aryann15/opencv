import cv2 as cv

img = cv.imread('Photos/cat1.jpeg')
cv.imshow('Cat',img)

#converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grayscale',gray)

# Blur
blur = cv.GaussianBlur(img,(3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)
cv.waitKey(0)

