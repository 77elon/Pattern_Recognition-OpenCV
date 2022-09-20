import time
import numpy as np, cv2 as cv

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

def scaling_nearest(img, size):
    dst = np.zeros(size[::-1], img.dtype)
    # 원하는 해상도와 np의 coord가 다르므로, np에 맞춰준 것.
    ratioX, ratioY = np.divide(size[::-1], img.shape[:2])
    # 우리가 출력하고자 하는 해상도는 OpenCV coord에 기반한 보간을 하고 싶은 것이므로, 
    # i.shape, j.shape가 각 x, y인 것을 알고 있음에도 불구하고, 반대 해상도를 입력해줘야 한다.
    i = np.arange(0, size[1], 1)
    j = np.arange(0, size[0], 1)

    i, j = np.meshgrid(i, j)
    
    x, y = np.int32(i / ratioX), np.int32(j / ratioY)
    dst[i, j] = img[x, y]
    return dst
    
def time_check(func, img, size, title):
    start_time = time.perf_counter()
    ret_img = func(img, size)
    elapsed = (time.perf_counter() - start_time) * 1000
    print(title, '수행시간 = %0.2f ms' % elapsed)
    return ret_img

image = cv.imread('./images/scaling.jpg')
image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

if image is None: raise Exception('영상파일 읽기 에러')

size = (300, 400)

dst1 = time_check(scaling, image, size, '방법1) 전방행렬 방식')
dst2 = time_check(scaling2, image, size, '방법2) 반복문 방식')
dst3 = scaling_nearest(image, size)
dst4 = cv.resize(image, size)


cv.imshow('image', image)
cv.imshow('scaling', dst1)
cv.imshow('scaling2', dst2)
cv.imshow('scaling_nearest', dst3)
cv.imshow('opencv resize', dst4)

cv.waitKey()





