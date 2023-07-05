import cv2 as cv

# img = cv.imread('Photos/cat1.jpeg')
#
# cv.imshow('1st Cat', img)
# cv.waitKey(0)

# READING VIDEOS
#
# capture = cv.VideoCapture('Videos/naruto1.gif')
#
# while True:
#     isTrue,frame = capture.read()
#     cv.imshow('Video',frame)
#     if cv.waitKey(20) &0xFF==ord('d'):
#         break
#
# capture.release()
# cv.destroyAllWindows()

# resizing and rescaling frames

import cv2 as cv

img = cv.imread('../Photos/cat1.jpeg')
cv.imshow('1st Cat', img)

def rescaleFrame (frame, scale=0.75):
    # photo, video , live video
    width = int(frame.shape[1]* scale)
    height= int(frame.shape[0]* scale)

    dimensions = (width,height)

    return cv.resize(frame,dimensions, interpolation = cv.INTER_AREA )
def changeRes (width,height):
    #live videos
    capture.set(3,width)
    capture.set(4,height)

frame_resized =rescaleFrame(img)
cv.imshow('frame resized', frame_resized )
cv.waitKey(0)