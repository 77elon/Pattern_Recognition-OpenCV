import numpy as np, cv2 as cv

def my_resize(logo, dsize, fx=0.0, fy=0.0):

    # dsize is none -> fx, fy ratio check
    if dsize is None:
        # 입력된 좌표, 배수에 따른 결과 매트릭스를 선언해줌.
        mat = np.zeros((int(logo.shape[0] * fx), int(logo.shape[1] * fy), 3), logo.dtype)
    # dsize check
    else:
        #np coord != cv coord
        mat = np.zeros((dsize[1], dsize[0], 3), logo.dtype)
    # 원본 이미지를 logo라고 인자를 선언했으므로,,, 
    # 해상도적인 관점에서 생각해봤을 때, 원본 이미지의 해상도와 대상 이미지의 해상도의 비율을 구한다면,
    # Nearest Interpolation을 구할 수 있게 된다.
    old_h, old_w, _ = logo.shape
    new_h, new_w, _ = mat.shape
    x_scale = (new_h / old_h)
    y_scale = (new_w / old_w)
    # 단순하게 원본 이미지의 x, y coord를 구해 대상 이미지의 픽셀 데이터에 채워준다.
    for i in range(mat.shape[0]):
        for n in range(mat.shape[1]):
            x = (int)(i / x_scale)
            y = (int)(n / y_scale)
            mat[i, n] = logo[x, y]
            #print(logo[index1, index2])
    return mat

image = cv.imread("./images/write_test.jpg", cv.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 오류")

img1 = cv.resize(image, (800, 600), fx=0.0, fy=0.0, interpolation= cv.INTER_NEAREST)
img2 = my_resize(image, (800, 600), fx=0.0, fy=0.0)
#img2 = my_resize(image, None, fx=2.0, fy=2.0)

cv.imshow("cv.resize", img1)
cv.imshow("my_resize", img2)

cv.waitKey(0)
cv.destroyAllWindows()