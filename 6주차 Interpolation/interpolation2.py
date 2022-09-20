import numpy as np, cv2

image = cv2.imread("./images/color.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("파일 에러")

x = 200
y = 800

# 결국 dsize가 있다면, fx, fy 생략 가능.
#fx는 horizontal axis 1, cols를 말하며, dim 0을 칭함.
#fy는 vertical axis 0, row를 말하며, dim 1을 칭함.
image2 = cv2.resize(image, dsize=(y, x), interpolation= cv2.INTER_NEAREST)
image3 = np.zeros((x, y, 3), image.dtype)

for i in range(image3.shapes[0]):
    for n in range(image3.shape[1]):
        index1 = (int) (i / 2)
        index2 = (int) (n / 2)
        image3[i][n] = image[index1][index2]





cv2.imshow("inter1", image2)
cv2.imshow("inter2", image3)

cv2.waitKey(0)

