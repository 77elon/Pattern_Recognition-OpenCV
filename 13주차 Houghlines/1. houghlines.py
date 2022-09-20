from idna import valid_contextj
from matplotlib.pyplot import polar
import numpy as np, cv2, math
def accumulate(image, rho, theta):
    h, w = image.shape[:2]
    # ary size is [height + width][180(pi)]
    rows, cols = (h + w) * 2 // rho, int(np.pi / theta)
    # 누적 행렬 선언
    acc_ary = np.zeros((rows, cols), dtype=np.int32)

    # t * theta, pi에 이동 각도를 대입하여, 삼각 함수 값을 구한다.
    sin_cos = [(np.sin(t * theta), np.cos(t * theta)) for t in range(cols)]
    # 값이 존재한는 것만...
    pts = np.where(image > 0)
    # 삼각함수와 값이 들어간 이미지의 행렬 곱 연산을 통해 극 좌표값을 구한다.
    polars = np.dot(sin_cos, pts).T
    polars = (polars / rho + rows / 2).astype(int)

    # row (pi) 만큼 연산한다.
    for row in polars:
        for t, r in enumerate(row):
            acc_ary[r, t] += 1
    return acc_ary

def masking(acc_ary, h, w, thresh):
    rows, cols = acc_ary.shape[:2]
    rcenter, tcenter = h//2, w//2
    dst = np.zeros(acc_ary.shape, dtype=np.uint)

    for y in range(0, rows, h):
        for x in range(0, cols, w):
            roi = acc_ary[y:y+h, x:x+w]
            _, max, _, (x0, y0) = cv2.minMaxLoc(roi)
            dst[y+y0, x+x0] = max
    return dst

def select_lines(acc_dst, rho, theta, thresh):
    rows = acc_dst.shape[0]
    r, t = np.where(acc_dst > thresh)

    rhos = ((r - (rows / 2)) * rho)
    radians = t * theta
    values = acc_dst[r, t]

    idx = np.argsort(values)[::-1]
    lines = np.transpose([rhos, radians])
    lines = lines[idx, :]

    return np.expand_dims(lines, axis=1)

def houghLines(src, rho, theta, thresh):
    acc_mat = accumulate(src, rho, theta)  # 허프 누적 행렬 계산
    acc_dst = masking(acc_mat, 7, 3, thresh)  # 마스킹 처리 7행,3열
    lines = select_lines(acc_dst, rho, theta, thresh)  # 직선 가져오기
    return lines

def draw_houghLines(src, lines, nline):
    dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)  # 컬러 영상 변환
    min_length = min(len(lines), nline)

    for i in range(min_length):
        rho, radian = lines[i, 0, 0:2]  # 수직거리 , 각도 - 3차원 행렬임
        a, b = math.cos(radian), math.sin(radian)
        pt = (a * rho, b * rho)  # 검출 직선상의 한 좌표 계산
        delta = (-1000 * b, 1000 * a)  # 직선상의 이동 위치
        pt1 = np.add(pt, delta).astype('int')
        pt2 = np.subtract(pt, delta).astype('int')
        cv2.line(dst, tuple(pt1), tuple(pt2), (0, 255, 0), 2, cv2.LINE_AA)

    return dst

image = cv2.imread('./images/hough.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 에러")
blur  = cv2.GaussianBlur(image, (5, 5), 2, 2)
canny = cv2.Canny(blur, 100, 200, 5)

rho, theta = 1,  np.pi / 180
lines1 = houghLines(canny, rho, theta, 80)
lines2 = cv2.HoughLines(canny, rho, theta, 80)
dst1 = draw_houghLines(canny, lines1, 7)
dst2 = draw_houghLines(canny, lines2, 7)

cv2.imshow("image", image)
cv2.imshow("canny", canny)
cv2.imshow("detected lines", dst1)
cv2.imshow("detected lines_OpenCV", dst2)
cv2.waitKey(0)