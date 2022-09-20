import cv2

title1, title2 = '16 bit unchanged', '32bit unchanged'
color2unchanged1 = cv2.imread("./images/read_16.tif", cv2.IMREAD_UNCHANGED)
color2unchanged2 = cv2.imread("./images/read_32.tif", cv2.IMREAD_UNCHANGED)

if color2unchanged1 is None or color2unchanged2 is None:
    raise Exception("영상 파일 읽기 에러")

