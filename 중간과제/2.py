import numpy as np, cv2 as cv

image = cv.imread("./images/color.jpg", cv.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 오류")

# 이미지의 컬러 채널을 분리하였음.
img = cv.split(image)
clr = np.zeros(image.shape[:2], dtype=np.uint8)

# 단일 채널의 출력을 해줌으로, Color Filter를 사용하지 않음에도, 채널의 색상을 출력할 수 있다.
cv.imshow("Blue Channel", cv.merge([img[0], clr, clr]))
cv.imshow("Green Channel", cv.merge([clr, img[1], clr]))
cv.imshow("Red Channel", cv.merge([clr, clr, img[2]]))

cv.waitKey(0)
cv.destroyAllWindows()