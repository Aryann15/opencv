import cv2 as cv
import numpy as np

img= cv.imread('../Photos/cat1.jpeg')
cv.imshow('cat',img)

b,g,r = cv.split(img)

cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)

print(img.shape) #(360, 474, 3)
print(b.shape) #(360, 474)

merged = cv.merge([b,g,r])
cv.imshow('merged',merged)

# actual color image
blank= np.zeros(img.shape[:2], dtype='uint8')
blue = cv.merge ([b,blank,blank])
green = cv.merge ([blank,g,blank])
red = cv.merge ([blank,blank,r])

cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)

cv.waitKey(0)