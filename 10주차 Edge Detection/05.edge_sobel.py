import numpy as np, cv2 as cv

img = cv.imread('./images/edge.jpg', cv.IMREAD_GRAYSCALE)

# 가로, 세로 마스크를 선언하였으며, 가중값이 2배 높다.
# 이로 인해 중심화소의 Weight가 높아지고, 대각선 방향의 에지 검출 가능성이 높아짐.
mask1 = np.array([-1, 0, 1, -2, 0, 2, -1, 0, 1], dtype=np.float64).reshape(3, 3)
mask2 = np.array([-1, -2, -1, 0, 0, 0, 1, 2, 1], dtype=np.float64).reshape(3, 3)

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

#shape[0], dx gradient
dst3 = cv.convertScaleAbs(cv.Sobel(np.float32(img), cv.CV_32F, 1, 0, 3))
dst4 = cv.convertScaleAbs(cv.Sobel(np.float32(img), cv.CV_32F, 0, 1, 3))

cv.imshow('dst1 - vertical mask', dst1)
cv.imshow('dst2 - horizonal mask', dst2)
cv.imshow('dst3 - vertical mask_OpenCV', dst3)
cv.imshow('dst2 - horizonal mask_OpenCV', dst4)

cv.waitKey()