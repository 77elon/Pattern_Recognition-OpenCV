import numpy as np, cv2 as cv

def average_filter(image, ksize):
    #shape[0] is rows, shape[1] is cols
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.uint8)
    # 무조건 Center 값을 알아야 함.
    center = ksize // 2

    for i in range(center, rows - center):
        for j in range(center, cols - center):
            y1, y2 = i - center, i + 1 + center
            x1, x2 = j - center, j + 1 + center
            #constraint border
            if y1 < 0 or y2 > rows or x1 < 0 or x2 > cols:
                dst[i, j] = image[i, j]
            else:
                mask = image[y1:y2, x1:x2]
                dst[i, j] = cv.mean(mask)[0]

    return dst

image = cv.imread('./images/filter_avg.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

avg_img = average_filter(gray, 5)
blur_img = cv.blur(gray, (5, 5), cv.BORDER_REFLECT)
box_img = cv.boxFilter(gray, ddepth=-1, ksize=(5, 5))

cv.imshow('image', image)
cv.imshow('avg_img', avg_img)
cv.imshow('blur_img', blur_img)
cv.imshow('box_img', box_img)

cv.waitKey()
