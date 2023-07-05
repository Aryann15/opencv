import cv2 as cv

img = cv.imread('../Photos/cat1.jpeg')
cv.imshow('Cat',img)

#converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('grayscale',gray)

# Blur
blur = cv.GaussianBlur(img,(3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Edge cascade
canny = cv.Canny(blur  ,125,175)
cv.imshow('Canny edges', canny)

#dilating the images
dilated= cv.dilate(canny, (3,3),iterations=1)
cv.imshow('dilated', dilated)

#eroded
eroded = cv.erode(dilated,(3,3),iterations= 1)
cv.imshow('eroded',eroded)

#Resize

resize = cv.resize(img,(500,500))
cv.imshow('resized',resize)

#cropping
cropped = img[50:200 , 200:400]
cv.imshow('cropped',cropped)
cv.waitKey(0)

