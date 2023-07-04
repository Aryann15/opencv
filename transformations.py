import numpy as np
import cv2 as cv

img= cv.imread('Photos/cat1.jpeg')
cv.imshow('cat', img)

#translation
def translate(img,x,y):
    transMat= np.float32 ([[1,0,x],[0,1,y]])
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimension)

translated = translate(img, 100 ,100)
cv.imshow('Translated', translated)

# -x => left
# -y => up
# x => right
# y => down

#rotation

def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2 , height //2)

    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat , dimensions)

rotated = rotate(img, 45)
cv.imshow('rotated', rotated)
cv.waitKey(0)