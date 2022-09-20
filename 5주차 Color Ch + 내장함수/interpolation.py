import math
import numpy as np, cv2

image = cv2.imread("./images/read_color.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("파일 에러")

mat1 = cv2.resize(image, (image.shape[1]*2,image.shape[0]*2), interpolation= cv2.INTER_LINEAR)
#mat1 = cv2.resize(image, (2.0, 2.0), interpolation = cv2.INTER_CUBIC)
mat2 = np.zeros((image.shape[0]*2,image.shape[1]*2, 3), image.dtype)

for i in range(mat2.shape[0]):
    for n in range(mat2.shape[1]):
        old_h, old_w, c = image.shape
        new_h, new_w, c = mat2.shape
        x_scale = (new_h / old_h)
        y_scale = (new_w / old_w)

        x = (int)(i / x_scale)
        y = (int)(n / y_scale)
        
        mat2[i][n] = image[x][y]


cv2.imshow("inter1", mat1)
cv2.imshow("inter2", mat2)

cv2.waitKey(0)
cv2.destroyAllWindows()