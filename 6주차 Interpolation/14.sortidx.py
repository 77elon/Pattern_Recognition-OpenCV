import numpy as np, cv2 as cv

m = np.random.randint(0, 100, 15).reshape(3, 5)

m_sort1 = cv.sortIdx(m, cv.SORT_EVERY_ROW)
m_sort2 = cv.sortIdx(m, cv.SORT_EVERY_COLUMN)
#axis 0 is cv shape 1 열 정렬(y)
m_sort3 = np.argsort(m, axis=0)

print (m)
print(m_sort1)
print(m_sort2)
print(m_sort3)
