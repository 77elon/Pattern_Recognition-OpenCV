from turtle import back
import numpy as np
import cv2 as cv

image = cv.imread('./images/bit_test.jpg')
logo = cv.imread('./images/logo.jpg')

if image is None or logo is None: raise Exception('영상 파일 읽기 오류')

#Logo의 색 정보를 모두 흰색으로 바꾼 마스크
masks = cv.threshold(logo, 220, 255, cv.THRESH_BINARY)[1]
masks = cv.split(masks)

#이후 마스크가 가지는 모든 색 채널의 값을 더함으로, Feature를 추출하고, Pass Filter를 만들 수 있다.
fg_pass_mask = cv.bitwise_or(masks[0], masks[1])
fg_pass_mask = cv.bitwise_or(fg_pass_mask, masks[2])
bg_pass_mask = cv.bitwise_not(fg_pass_mask)

(H, W), (h, w) = image.shape[:2], logo.shape[:2]
x, y = (W - w) // 2, (H - h) // 2
roi = image[y:y+h, x:x+w]

# foreground Pass Filter는 색 정보를 가지는 특성만 통과 시킬 수 있으므로, 로고 이미지와 같은 화면이 출력될 것.
# But, 분리된 상태라는 것만 인지...
foreground = cv.bitwise_and(logo, logo, mask= fg_pass_mask)
# Background Pass Filter의 경우, 로고의 색 특성을 제외한 화면만 통과할 수 있으므로, 중간에 로고가 통과되지 못해, 검은색의 로고와 Background가 출력될 것이다.
background = cv.bitwise_and(roi, roi, mask=bg_pass_mask)

# 순수한 로고와 백그라운드 이미지를 합치는 방법은 좋은 방법은 아니다.
# 그러나, 같은 Pass Filter, Mask로 통과 시켰으며, Projection 또한 실시하지 않았으므로, 
# 우리가 원하는 워터마크만 추가하는 화면이 출력될 것이다.

dst = cv.add(background, foreground)
image[y:y+h, x:x+w] = dst

cv.imshow('fg_pass_mask', fg_pass_mask)
cv.imshow('background', background)
cv.imshow('foreground', foreground)
cv.imshow('dst', dst)
cv.waitKey(0)
cv.destroyAllWindows()
