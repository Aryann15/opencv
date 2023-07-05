import cv2 as cv
import matplotlib.pyplot as plt

img= cv.imread('../Photos/cat1.jpeg')
cv.imshow('cats',img)

# plt.imshow(img)
# plt.show()
#
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# BGR TO HSV(hue stauration value)
hsv= cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

# BGR to L*A*B
lab= cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

plt.imshow(rgb)
plt.show() #inversion of color

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('hsv to bgr' , hsv_bgr)


cv.waitKey(0)