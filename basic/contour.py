import cv2 as cv
import numpy as np

img= cv.imread('../Photos/cat1.jpeg')

cv.imshow('cat',img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('gray',gray)

# blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
# cv.imshow('blur',blur)
#
# canny = cv.Canny(blur,125,175)
# cv.imshow('canny',canny)
#
# contours, hierarchy = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
# print(f'{len(contours)} contours found ')

ret,thresh = cv.threshold(gray,125,255, cv.THRESH_BINARY)
cv.imshow('thresh',thresh)

contours,hierarshies = cv.findContours(thresh,cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found ')

blank = np.zeros(img.shape,dtype='uint8')
cv.imshow('blank',blank)

draw = cv.drawContours(blank,contours, -1, (0,0,255),1)
cv.imshow('drawnc contours',draw)

cv.waitKey(0)