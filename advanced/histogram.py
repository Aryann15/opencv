import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('../Photos/cat1.jpeg')
cv.imshow('cats',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GRAY',gray)

# Grayscale histogram
# gray_hist = cv.calcHist([gray],[0], None, [256],[0,256])
# plt.figure()
# plt.title('Grayscale Histograms')
# plt.xlabel('Bins')
# plt.ylabel('no of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Color Histogram
plt.figure()
plt.title('Grayscale Histograms')
plt.xlabel('Bins')
plt.ylabel('no of pixels')
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],None,[256],[0,256] )
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()
cv.waitKey(0)