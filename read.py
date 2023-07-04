import cv2 as cv

# img = cv.imread('Photos/cat1.jpeg')
#
# cv.imshow('1st Cat', img)
# cv.waitKey(0)

#READING VIDEOS

capture = cv.VideoCapture('Videos/naruto1.gif')

while True:
    isTrue,frame = capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) &0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()