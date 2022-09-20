import numpy as np, cv2 as cv

img = cv.imread('./images/laplacian.jpg', cv.IMREAD_GRAYSCALE)

mask1 = np.array(
    [0, 1, 0, 
    1, -4, 1, 
    0, 1, 0], dtype=np.float64).reshape(3, 3)
mask2 = np.array(
    [-1, -1, -1, 
    -1, 8, -1, 
    -1, -1, -1], dtype=np.float64).reshape(3, 3)

mask1_1 = np.array(mask1, np.int16)
mask2_1 = np.array(mask2, np.int16)

# Laplacian is L2Gradiant edge detection method...
dst1 = cv.filter2D(img, cv.CV_16S, mask1_1)
dst2 = cv.filter2D(img, cv.CV_16S, mask2_1)
dst3 = cv.Laplacian(img, cv.CV_16S, 1)

cv.imshow('image', img)
cv.imshow('filter2D 4-Direction', cv.convertScaleAbs(dst1))
cv.imshow('filter2D 8-Direction', cv.convertScaleAbs(dst2))
cv.imshow('Laplacian_OpenCV', cv.convertScaleAbs(dst3))

cv.waitKey(0)
