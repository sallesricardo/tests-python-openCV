import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(cv.imread('photos/car.jpg'), scale=0.25)
cv.imshow('Car', img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average', average)

# Gaussian Blur
gaussian = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian', gaussian)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 15, 35, 25)
cv.imshow('Bilateral', bilateral)


cv.waitKey(0)