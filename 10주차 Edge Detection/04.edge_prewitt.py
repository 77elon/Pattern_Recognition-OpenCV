import numpy as np, cv2 as cv

img = cv.imread('./images/edge.jpg')

# 수직 마스크, 수평 마스크 선언.
mask1 = np.array([-1, 0, 1, -1, 0, 1, -1, 0, 1], dtype=np.float64).reshape(3, 3)
mask2 = np.array([-1, -1, -1, 0, 0, 0, 1, 1, 1], dtype=np.float64).reshape(3, 3)

def differential():
    global img, mask1, mask2

    #dst1 = cv.filter2D(img, cv.CV_64F, mask1)
    #dst2 = cv.filter2D(img, cv.CV_64F, mask2)
    #dst = cv.magnitude(dst1, dst2)

    dst1 = cv.convertScaleAbs(cv.filter2D(img, cv.CV_64F, mask1))
    dst2 = cv.convertScaleAbs(cv.filter2D(img, cv.CV_64F, mask2))

    dst = cv.addWeighted(dst1, 1, dst2, 1, 0.0)

    return dst, dst1, dst2

dst, dst1, dst2 = differential()
cv.imshow('dst', dst)
cv.imshow('dst1', dst1)
cv.imshow('dst2', dst2)

cv.waitKey(0)
