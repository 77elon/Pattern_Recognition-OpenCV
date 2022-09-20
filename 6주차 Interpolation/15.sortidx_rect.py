from cmath import rect
from statistics import mean
import numpy as np, cv2 as cv

def print_rects(rects):
    print('-' * 46)
    print('사각형 원소 \t 랜덤 사각형 정보 \t 크기')
    print('-' * 46)
    for i, (x, y, w, h, a) in enumerate(rects):
        print('rects[%i] = [(%3d, %3d) from (%3d, %3d)] %5d' %(i, x, y, w, h, a))

rands = np.zeros((5, 5), dtype=np.uint16)
# at [][0, 1]
starts = cv.randn(rands[:, :2], mean=100, stddev=50)
#at [][2,3]
ends = cv.randn(rands[:, 2:-1], mean=300, stddev=50)

#starts.shapes[1] is 2 and ends.shapes[1] is 2 ,too
#sizes.shapes is [][2]
areas = cv.absdiff(starts, ends)

#여기서는 사각형을 결정하는 두 점을 [][0], [][1]로 결정하였음.
sizes = areas[:, 0] * areas[:, 1]
rects = rands.copy()

#rects[][2:3] stored area, point(x, y)
rects[:, 2:-1] = areas

# [][4] is 넓이... 
rects[:, -1] = sizes

#간단하다. 넓이의 오름차순으로 정렬하기 위해, [][4]에 저장된 데이터의 크기 순서를 알아내면 끝이다.
#y축을 기준으로, axis 0을 기준으로 dim 1을 기준으로 정렬하고, 그 인덱스의 순서를 idx에 저장한다.
idx = cv.sortIdx(sizes, cv.SORT_EVERY_COLUMN).flatten()

#sortIdx 함수로 알아낸 인덱스 순서를 통해, rects에 접근하고 이에 대한 정보를 출력해주면 끝이다.
#실질적으로는 np에서 제공하는 rects[5,4,1,2,3]과 같은 형식으로 전달된 것이며, 함수는 0~4의 순서로 들어왔다고 인식하게 된다.
print_rects(rects)
print_rects(rects[idx.astype(int)])