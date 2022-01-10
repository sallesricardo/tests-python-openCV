import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(cv.imread('photos/car.jpg'), scale=0.25)
cv.imshow('Car', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(img, (7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edge', canny)

dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('Dilate', dilated)

eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow('Erode', eroded)

croped = img[50:200, 200:400]
cv.imshow('Crop', croped)

cv.waitKey(0)