import numpy as np, cv2 as cv
from module import rotate_pt

def calc_angle(pt):
    d1 = np.subtract(pt[1], pt[0]).astype(np.float32)
    d2 = np.subtract(pt[2], pt[0]).astype(np.float32)
    angle1 = cv.fastAtan2(d1[1], d1[0])
    angle2 = cv.fastAtan2(d2[1], d2[0])

    # radian
    return (angle2 - angle1)

def draw_point(width, height):
    global pt, tmp
    # cv coord
    pt.append([width, height])
    print('좌표: ', len(pt), [height, width])
    cv.circle(tmp, (width, height), 2, 255, 2)
    cv.imshow('image', tmp)

def onMouse(event, width, height, flags, param=None):
    global title, pt, tmp, image

    if event == cv.EVENT_LBUTTONDOWN and len(pt) == 1:
        draw_point(width, height)
    elif event == cv.EVENT_LBUTTONUP and (len(pt) != 1):
        draw_point(width, height)

    if len(pt) == 3:
        angle = calc_angle(pt)
        print('회전각: %3.2f' % angle)
        dst = rotate_pt(image, (angle), pt[0])
        cv.imshow('image', dst)
        tmp = image.copy()
        pt = []

image = cv.imread('./images/rotate.jpg', cv.IMREAD_GRAYSCALE)
if image is None: raise Exception('영상파일 읽기 에러')

tmp = image.copy()
pt = []
title = 'image'
cv.imshow(title, image)
cv.setMouseCallback(title, onMouse, 0)


cv.waitKey()