import numpy as np, cv2 as cv

image1 = np.zeros((50, 512), dtype=np.uint8)
image2 = np.zeros((50, 512), dtype=np.uint8)

rows, cols = image1.shape[:2]

for i in range(rows):
    for j in range(cols):
        image1.itemset((i, j), j // 2)
        #Operator Scaling Sequence diff...
        image2.itemset((i, j), j // 20 * 10)

cv.imshow("image1", image1)
cv.imshow("image2", image2)

cv.waitKey(0)
cv.destroyAllWindows()


