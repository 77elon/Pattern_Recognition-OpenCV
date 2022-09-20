import numpy as np, cv2 as cv

image1 = cv.imread('./images/pixel.jpg', cv.IMREAD_GRAYSCALE)
if image1 is None: raise Exception("영상 파일 읽기 오류")

# 마우스 콜백을 위해 선언
title = 'result'
pt = (-1, -1)

def draw_hist(img, shape=(200, 256)):
    # 히스토그램 내장 함수를 사용하여, 조건에 맞게 히스토그램 크기를 32로 설정하였음.
    hist = cv.calcHist([img], [0], None, [32], [0, 256])
    # graph mat declare
    hist_img = np.full(shape, 255, np.uint8)
    # 히스토그램이 가지는 데이터를 x축(cv 좌표계 기준)의 크기에 맞게 정규화하였음.
    cv.normalize(hist, hist, 0, shape[0], cv.NORM_MINMAX)
    # 히스토그램 출력 매트릭스 크기(cv 좌표계 기준 y축, 가로 축)에 맞추기 위해 multiply 값을 구함.
    gap = hist_img.shape[1] / hist.shape[0]

    # hist에 저장된 값을 가져와, (0, x) -> (int(h), w)에 직사각형을 그려줌으로, 히스토그램을 표현해 줄 수 있다.
    # 그러나, cv 좌표계는 [x][y][z] 순서로 사용되므로, 우리가 인지하는 것과 같이 표현하려고 할 때는,  shape[0], shape[1] 데이터를 바꿔서 적게 된다.
    # 그게 26번 행, 직사각형 그리는 함수에도 적용된다.
    for i, h in enumerate(hist):
        x = int(round(i * gap))
        w = int(round(gap))
        cv.rectangle(hist_img, (x, 0, w, int(h)), (0, 0, 0), cv.FILLED)
    # cv coordinate 관점에서 왼쪽 위부터 시작되므로, 데이터를 배치해주고, 마지막에 반전된 mat를 반환한다.
    return cv.flip(hist_img, 0)


def onMouse(event, x, y, flags, param=None):
    # Callback 반환 이후, 함수 내 저장된 좌표 값이 지워지므로, 전역 변수를 선언하였음.
    global title, pt, image1

    # 좌 클릭 이벤트가 들어왔을 때, 그리고 이전에 입력된 혹은 저장된 마우스 클릭 좌표가 유효하지 않거나 존재하지 않는다면, 좌표를 저장한다.
    if event == cv.EVENT_LBUTTONDOWN:
        if pt[0] < 0:
            #pt is previous click point
            pt = (x, y)
        # 반대의 경우, 이전에 입력된 좌표를 기준으로 검은 직사각형을 그리게 된다.
        else:
            cv.rectangle(image1, pt, (x, y), (0, 0, 0), 2)
            
            # 마우스 클릭으로 선택된 이미지의 전달을 위해, 슬라이싱으로 추출하였음.
            selected = []
            if pt[1] < y: selected = image1[pt[1]:y, pt[0]:x]
            else: selected = image1[pt[1]:y:-1, pt[0]:x:-1]

            cv.imshow(title, image1)
            # 선택된 이미지를 히스토그램을 그리는 함수로 전달하고, 반환된 mat를 통해, 히스토그램을 그려준다.
            cv.imshow('hist_img', draw_hist(selected))
            #print(pt, x, y)
            #cv.imshow('selected', selected)
            pt = (-1, -1)

cv.imshow(title, image1)
cv.setMouseCallback(title, onMouse)
cv.waitKey(0)
cv.destroyAllWindows()