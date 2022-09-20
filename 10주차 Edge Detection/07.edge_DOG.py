import numpy as np, cv2 as cv

img = cv.imread('./images/dog.jpg', cv.IMREAD_GRAYSCALE)

gaus = cv.GaussianBlur(img, (7, 7), 0, 0)
dst1 = cv.Laplacian(gaus, cv.CV_64F, 7)

gaus1 = cv.GaussianBlur(img, (3, 3), 0)
gaus2 = cv.GaussianBlur(img, (9, 9), 0)
dst2 = gaus1 - gaus2

cv.imshow('image', img)
# Noise Removal -> edge detection
cv.imshow('dst1 - LoG (Gaussian -> Laplacian)', dst1.astype('uint8'))
# Gaussian Smoothing Filtering difference
cv.imshow('dst2 - DoG(Gaussian ksize = (3, 3) - Gaussian ksize = (9, 9)', dst2)

cv.waitKey()