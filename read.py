import cv2 as cv

img = cv.imread('Photos/cat1.jpeg')

cv.imshow('1st Cat', img)

cv.waitKey(0)