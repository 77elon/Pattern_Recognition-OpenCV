import numpy as np, cv2 as cv

img = cv.imread('./images/filter_blur.jpg')

mask = np.full((3, 3), 1/9, dtype=np.float32)
blur = cv.filter2D(img, -1, mask)

cv.imshow('img', img)
cv.imshow('blur', blur)

cv.waitKey(0)