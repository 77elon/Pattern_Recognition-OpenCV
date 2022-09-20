import numpy as np, cv2 as cv
image = cv.imread('./images/sum_test.jpg')

mask = np.zeros((image.shape[:2]), dtype=np.uint8)
mask[60:160, 20:120] = 255

sum_value = cv.sumElems(image)
mean_value1 = cv.mean(image)
mean_value2 = cv.mean(image, mask= mask)

print(type(sum_value), type(sum_value[0]))
print(sum_value)
print(mean_value1)
print(mean_value2)

mean, stddev = cv.meanStdDev(image)
mean2, stddev2 = cv.meanStdDev(image, mask=mask)

print(type(mean), type(mean[0][0]))
print(mean2.flatten())
print(stddev2.flatten())

cv.imshow('image', image)
cv.imshow('mask', mask)
cv.waitKey(0)
cv.destroyAllWindows()
