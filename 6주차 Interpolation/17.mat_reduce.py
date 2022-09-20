import numpy as np, cv2 as cv

m = np.random.rand(3, 5) * 1000//10

#dim is shapes[n] 기준으로 정리하는 것.
#dim 0 is x axis 기준으로 정리하는 것. 즉, 열 정리
reduce_sum = cv.reduce(m, dim=0, rtype=cv.REDUCE_SUM)
reduce_avg = cv.reduce(m, dim=1, rtype=cv.REDUCE_AVG)
reduce_max = cv.reduce(m, dim=0, rtype=cv.REDUCE_MAX)
reduce_min = cv.reduce(m, dim=1, rtype=cv.REDUCE_MIN)

print(m)
print(reduce_sum.flatten())
print(reduce_avg.flatten())
print(reduce_max.flatten())
print(reduce_min.flatten())

