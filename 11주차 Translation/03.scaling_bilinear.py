import numpy as np, cv2 as cv
from module import scaling_nearest

def bilinear_value(img, pt):
    x, y = np.int32(pt)
    # 만약 확대라면, 대상 크기의 (-1, -1)을 실시한다... 테두리 영상 범위 벗어남 처리?
    if x >= img.shape[1] - 1: x = x - 1
    if y >= img.shape[0] - 1: y = y - 1 

    # [[[229 219 209]
    # [231 219 209]]

    # [[229 219 209]
    # [231 220 212]]]
    #P1, P2, P3, P4 = np.float32(img[y:y+2, x:x+2].flatten()) 

    P1 = np.array(img[y, x], dtype=np.float32)
    P2 = np.array(img[y + 0, x + 1], dtype=np.float32)
    P3 = np.array(img[y + 1, x + 0], dtype=np.float32)
    P4 = np.array(img[y + 1, x + 1], dtype=np.float32)

    alpha, beta = pt[1] - y, pt[0] - x
    M1 = P1 + alpha * (P3 - P1)
    M2 = P2 + alpha * (P4 - P2)
    P = M1 + beta * (M2 - M1)
    #return value clipping(limit)
    return np.clip(P, 0, 255)

def scaling_bilinear(img, size):
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])

    dst = [[bilinear_value(img, (j / ratioX, i / ratioY))   for j in range(size[0])]    for i in range(size[1])]
    return np.array(dst, img.dtype)

image = cv.imread('./images/interpolation.jpg', cv.IMREAD_GRAYSCALE)
if image is None: raise Exception('영상파일 읽기 에러')

size = (300, 400)
dst1 = scaling_bilinear(image, size)
dst2 = scaling_nearest(image, size)
dst3 = cv.resize(image, size, 0, 0, cv.INTER_LINEAR)
dst4 = cv.resize(image, size, 0, 0, cv.INTER_NEAREST)


cv.imshow('image', image)
cv.imshow('User_bilinear', dst1)
cv.imshow('User_Nearest', dst2)
cv.imshow('OpenCV_bilinear', dst3)
cv.imshow('OpenCV_Nearest', dst4)

cv.waitKey()
