import numpy as np, cv2 as cv

def minmax_filter(image, ksize, mode):
    #shape[0] is rows, shape[1] is cols
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.uint8)
    # 무조건 Center 값을 알아야 함.
    center = ksize // 2

    for i in range(center, rows - center):
        for j in range(center, cols - center):
            y1, y2 = i - center, i + 1 + center
            x1, x2 = j - center, j + 1 + center
            if y1 < 0 or y2 > rows or x1 < 0 or x2 > cols:
                dst[i, j] = image[i, j]
            else:
                mask = image[y1:y2, x1:x2]
                dst[i, j] = cv.minMaxLoc(mask)[mode]

    return dst

image = cv.imread('./images/min_max.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
minfilter_img = minmax_filter(gray, 3, 0)
maxfilter_img = minmax_filter(gray, 3, 1)

cv.imshow('image', gray)
cv.imshow('minfilter_img', minfilter_img)
cv.imshow('maxfilter_img', maxfilter_img)

cv.waitKey()