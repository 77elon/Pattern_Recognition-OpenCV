import numpy as np
import cv2

image = cv2.imread("images/flip_test.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("에러")

image_x = np.zeros(image.shape,image.dtype)
image_y = np.zeros(image.shape,image.dtype)
image_xy = np.zeros(image.shape,image.dtype)
image_trans = np.zeros((image.shape[1],image.shape[0],image.shape[2]), image.dtype)

for i in range(image.shape[0]):
    for n in range(image.shape[1]):
        x_filp1 = (int) ((image.shape[0] - 1) - i)
        y_filp1 = (int) ((image.shape[1] - 1) - n)
        x = i
        y = n
        image_x[i][n] = image[x_filp1][y]
        image_y[i][n] = image[x][y_filp1]
        image_xy[i][n] = image[x_filp1][y_filp1]
        image_trans[n][i] = image[x][y]


cv2.imshow("original",image)
cv2.imshow("x_flip",image_x)
cv2.imshow("y_flip",image_y)
cv2.imshow("xy_flip",image_xy)
cv2.imshow("xy_trans",image_trans)


cv2.waitKey(0)
cv2.destroyAllWindows()


