import numpy as np, cv2 as cv

img = cv.imread('./images/filter_sharpen.jpg')

mask1 = np.array(
    [0, -1, 0, 
    -1, 5, -1, 
    0, -1, 0]
    , dtype=np.float32).reshape(3, 3)
mask2 = np.full((3, 3), -1, dtype=np.float32)
mask2[2, 2] = 9

sharpen1 = cv.filter2D(img, -1, mask1)
sharpen2 = cv.filter2D(img, -1, mask2)

cv.imshow('sharpen1', sharpen1)
cv.imshow('sharpen2', sharpen2)

cv.waitKey(0)