import numpy as np
import cv2 as cv

image = cv.imread('./images/minMax.jpg', cv.COLOR_BGR2GRAY)
if image is None: raise Exception('영상파일 읽기 오류 발생')

min_val, max_val, _, _ = cv.minMaxLoc(image)

#Normalize to 255 scale
ratio = 255 / abs(max_val - min_val)
dst = np.round((image - min_val) * ratio).astype(np.uint8)
min_dst, max_dst, _, _ = cv.minMaxLoc(dst)

print(min_val, max_val)
print(min_dst, max_dst)

cv.imshow('image', image)
cv.imshow('dst', dst)

cv.waitKey(0)
cv.destroyAllWindows()