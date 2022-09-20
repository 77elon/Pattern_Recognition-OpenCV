from lib2to3.pgen2 import grammar
import numpy as np, cv2 as cv

gray = cv.imread('./images/hist_stretch.jpg', cv.COLOR_BGR2GRAY)
if gray is None: raise Exception('영상 파일 읽기 오류')


minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(gray)

hist_img =(gray - minVal) / maxVal - minVal

hist_func = cv.equalizeHist(gray)

cv.imshow('hist_img', hist_img)
cv.imshow('hist_func', hist_func)

cv.waitKey(0)
cv.destroyAllWindows()