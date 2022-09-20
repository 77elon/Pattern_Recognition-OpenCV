import numpy as np, cv2 as cv
import time

def scaling(img, size):
    dst = np.zeros(size[::-1], img.dtype)
    
    # dst / origin (scale)
    ratioX, ratioY = np.divide(size[::-1], img.shape[:2])

    x = np.arange(0, img.shape[0], 1)
    y = np.arange(0, img.shape[1], 1)

    x, y = np.meshgrid(x, y)
    i, j = np.int32(x * ratioX), np.int32(y * ratioY)
    dst [i, j] = img[x, y]
    return dst

def scaling2(img, size):
    dst = np.zeros(size[::-1], img.dtype)
    ratioX, ratioY = np.divide(size[::-1], img.shape[:2])

    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            i, j = int(x * ratioX), int(y * ratioY)
            dst[i, j] = img[x, y]
    return dst


def time_check(func, img, size, title):
    start_time = time.perf_counter()
    ret_img = func(img, size)
    elapsed = (time.perf_counter() - start_time) * 1000
    print(title, '수행시간 = %0.2f ms' % elapsed)
    return ret_img

image = cv.imread('./images/scaling.jpg', cv.IMREAD_GRAYSCALE)
if image is None: raise Exception('영상파일 읽기 에러')

dst1 = time_check(scaling, image, (400, 400), '방법1) 전방행렬 방식')
dst2 = time_check(scaling2, image, (400, 400), '방법2) 반복문 방식')

cv.imshow('image', image)
cv.imshow('dst1 - (400, 400)', dst1)
cv.imshow('dst2 - (400, 400)', dst2)

cv.waitKey()