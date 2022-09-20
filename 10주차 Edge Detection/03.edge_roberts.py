import numpy as np, cv2 as cv

img = cv.imread('./images/edge.jpg')

# 1차 미분 로버츠 마스크, 대각선을 칭하는 마스크 2개 선언.
mask1 = np.zeros((3, 3), dtype=np.float64)
mask1[0][0] = -1.0
mask1[1][1] = 1.0

mask2 = np.zeros((3, 3), dtype=np.float64)
mask2[0][2] = -1.0
mask2[1][1] = 1.0

def differential():
    global img, mask1, mask2

    dst1 = cv.convertScaleAbs(cv.filter2D(img, cv.CV_64F, mask1))
    dst2 = cv.convertScaleAbs(cv.filter2D(img, cv.CV_64F, mask2))

    dst = cv.addWeighted(dst1, 1, dst2, 1, 0.0)
    
    # Not Working, 
    #dst = cv.magnitude(dst1, dst2)

    return dst, dst1, dst2

dst, dst1, dst2 = differential()
cv.imshow('dst', dst)
cv.imshow('dst1', dst1)
cv.imshow('dst2', dst2)

cv.waitKey(0)
