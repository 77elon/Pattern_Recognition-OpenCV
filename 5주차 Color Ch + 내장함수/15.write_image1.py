import cv2
import numpy as np


image = cv2.imread("./images/color.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 에러")

param_jpg = (cv2.IMWRITE_JPEG_QUALITY, 10)
param_png = [cv2.IMWRITE_PNG_COMPRESSION, 9]

cv2.imwrite("./images/write_test1.jpg", image)
cv2.imwrite("./images/write_test2.jpg", image, param_jpg)
cv2.imwrite("./images/write_test3.png", image,param_png)
cv2.imwrite("./images/write_test4.bmp", image)
cv2.imwrite("./images/write_test5.jpg", image, (cv2.IMWRITE_JPEG_QUALITY, 100))
cv2.imwrite("./images/write_test6.jpg", image, (cv2.IMWRITE_JPEG_QUALITY, 75))
cv2.imwrite("./images/write_test7.jpg", image, (cv2.IMWRITE_JPEG_QUALITY, 50))
cv2.imwrite("./images/write_test8.jpg", image, (cv2.IMWRITE_JPEG_QUALITY, 25))

image2 = np.zeros(image.shape, dtype=image.dtype)

cv2.resize(image, (200, 400), interpolation=cv2.INTER_LINEAR)
print("저장 완료")


