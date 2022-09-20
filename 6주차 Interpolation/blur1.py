from audioop import avg
import numpy as np, cv2

image = cv2.imread("./images/color.jpg", cv2.IMREAD_COLOR)
image_blur_normal = image.copy()
image_blur_abnormal = image.copy()
image_blur = cv2.blur(image, (5,5))


for i in range(image.shape[0] - 2):
    for n in range(image.shape[1] - 2):
        #4-plane 제외
        temp = image[i + 2 : i + 7, n + 2 : n + 7, :3]
        avg = cv2.reduce(temp, dim=0, rtype=cv2.REDUCE_AVG)
        #print(avg)
        result = cv2.reduce(avg, dim=1, rtype=cv2.REDUCE_AVG)
        #print(result)
        image_blur_abnormal[i][n] = cv2.mean(image[i + 2: i + 7, n + 2 : n + 7])[:3]# 4ch? BGRA?
        image_blur_normal[i][n] = result


cv2.imshow("normal", image_blur_normal)
cv2.imshow("abnormal", image_blur_abnormal)
cv2.imshow("blur func", image_blur)

cv2.waitKeyEx()

