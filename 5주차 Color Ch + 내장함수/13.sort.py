import numpy as np, cv2 as cv

m = np.random.randint(0, 100, 15).reshape(3, 5)

sort1 = cv.sort(m, cv.SORT_EVERY_ROW)
sort2 = cv.sort(m, cv.SORT_EVERY_COLUMN)
sort3 = cv.sort(m, cv.SORT_EVERY_ROW + cv.SORT_DESCENDING)
#np axis x축, 가로 방향 == cv에서의 dim 0
sort4 = np.sort(m, axis=1)
sort5 = np.sort(m, axis=0)
sort6 = np.sort(m, axis=1) [:, ::-1]

titles = ['m', 'sort1', 'sort2', 'sort3', 'sort4', 'sort5', 'sort6']

for title in titles:
    print(title, eval(title))