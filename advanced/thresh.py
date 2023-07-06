import cv2 as cv

img = cv.imread('../Photos/cat1.jpeg')
cv.imshow('Cat',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Simple Thresholding

threshold, thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('Simple Threshold',thresh)

threshold, thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Simple Inverse Threshold',thresh_inv)

#adaptive thresholding

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,3)
cv.imshow('adaptive threshold', adaptive_thresh)

cv.waitKey(0)