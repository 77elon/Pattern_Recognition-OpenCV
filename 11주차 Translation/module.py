import numpy as np

def scaling_nearest(img, size):
    dst = np.zeros(size[::-1], img.dtype)
    # 원하는 해상도와 np의 coord가 다르므로, np에 맞춰준 것.
    ratioX, ratioY = np.divide(size[::-1], img.shape[:2])
    # 우리가 출력하고자 하는 해상도는 OpenCV coord에 기반한 보간을 하고 싶은 것이므로, 
    # i.shape, j.shape가 각 x, y인 것을 알고 있음에도 불구하고, 반대 해상도를 입력해줘야 한다.
    i = np.arange(0, size[1], 1)
    j = np.arange(0, size[0], 1)

    i, j = np.meshgrid(i, j)
    
    x, y = np.int32(i / ratioX), np.int32(j / ratioY)
    dst[i, j] = img[x, y]
    return dst

def bilinear_value(img, pt):
    # input pt dtype is (width, height)
    x, y = np.int32(pt)
    # 만약 확대라면, 대상 크기의 (-1, -1)을 실시한다... 테두리 영상 범위 벗어남 처리?
    if x >= img.shape[1] - 1: x = x - 1
    if y >= img.shape[0] - 1: y = y - 1 

    # [[[229 219 209]
    # [231 219 209]]

    # [[229 219 209]
    # [231 220 212]]]
    #P1, P2, P3, P4 = np.float32(img[y:y+2, x:x+2].flatten()) 

    P1 = np.array(img[y, x], dtype=np.float32)
    P2 = np.array(img[y + 0, x + 1], dtype=np.float32)
    P3 = np.array(img[y + 1, x + 0], dtype=np.float32)
    P4 = np.array(img[y + 1, x + 1], dtype=np.float32)

    alpha, beta = pt[1] - y, pt[0] - x
    M1 = P1 + alpha * (P3 - P1)
    M2 = P2 + alpha * (P4 - P2)
    P = M1 + beta * (M2 - M1)
    #return value clipping(limit)
    return np.clip(P, 0, 255)

def contain(p, shape):
    return 0<= p[0] <shape[0] and 0 <= p[1] < shape[1]

# pt 기준 회전 변환 함수
def rotate_pt(img, degree, pt):
    dst = np.zeros(img.shape[:2], img.dtype)
    radian = np.deg2rad(degree)
    sin, cos = np.sin(radian), np.cos(radian)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # input pt dtype is (width, height), pre-translation based on pt
            jj, ii = np.subtract((j, i), pt)

            height = -jj * sin + ii * cos
            width = jj * cos + ii * sin

            # post-translation based on pt
            height, width = np.add((height, width), pt)

            if contain((height, width), img.shape):
                dst[i, j] = bilinear_value(img, (width, height))

    return dst