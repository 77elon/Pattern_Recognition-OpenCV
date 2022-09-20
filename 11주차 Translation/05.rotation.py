import numpy as np, cv2 as cv, math

from module import bilinear_value
from module import contain

def rotate(img, degree):
    dst = np.zeros(img.shape[:2], img.dtype)
    
    #radian = (degree / 180) * np.pi
    radian = np.deg2rad(degree)
    sin, cos = np.sin(radian), np.cos(radian)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # height is y(in math coord)
            height = -j * sin + i * cos
            width = j * cos + i * sin

            if (contain((height, width), img.shape)):
                #bilinear_value return (width, height)
                dst[i, j] = bilinear_value(img, (width, height))
                #dst[i, j] = img[height, width]

    return dst


# pt 기준 회전 변환 함수
def rotate_pt(img, degree, pt):
    dst = np.zeros(img.shape[:2], img.dtype)
    radian = np.deg2rad(degree)
    sin, cos = math.sin(radian), np.cos(radian)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # input pt dtype is (width, height), pre-translation based on pt
            jj, ii = np.subtract((j, i), pt)

            height = -jj * sin + ii * cos
            width = jj * cos + ii * sin

            # post-translation based on pt
            height, width = np.add((height, width), pt)

            if contain((height, width), img.shape):
                dst[i, j] = bilinear_value(img, (width, height))

    return dst


image = cv.imread('./images/rotate.jpg', cv.IMREAD_GRAYSCALE)
if image is None: raise Exception('영상파일 읽기 에러')

# 왜 역순의 좌표를 기반으로 작업하는 것일까?
# 이번에는 np coord 대신, opencv의 width, height 순서대로 정렬하여 중심 좌표를 추출하였다.
center = np.divmod(image.shape[::-1], 2)[0]
dst1 = rotate(image, 20)
dst2 = rotate_pt(image, 20, center)


cv.imshow('image', image)
cv.imshow('dst1: rotated on (0, 0) ', dst1)
cv.imshow('dst1: rotated on image of center point', dst2)

cv.waitKey()
