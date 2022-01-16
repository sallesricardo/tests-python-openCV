import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(cv.imread('photos/car.jpg'), scale=0.25)
cv.imshow('Car', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

mask = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked', masked)

cv.waitKey(0)