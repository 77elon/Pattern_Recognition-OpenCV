import enum
import numpy as np, cv2 as cv

def draw_histo(hist, shape=(200, 256)):
    hist_img = np.full(shape, 255, np.uint8)
    cv.normalize(hist, hist, 0, shape[0], cv.NORM_MINMAX)
    gap = hist_img.shape[1] / hist.shape[0]

    for i, h in enumerate(hist):
        x = int(round(i * gap))
        w = int(round(gap))
        cv.rectangle(hist_img, (x, 0), (w, int(h)), 0, cv.FILLED)
    return cv.flip(hist_img, 0)


image = cv.imread('./images/pixel.jpg')
if image is None: raise Exception('영상 파일 읽기 오류')

histSize, ranges = [32], [0, 256]
gap = ranges[1] / histSize[0]
ranges_gap = np.arange(0, ranges[1] + 1, gap)
hist1 = cv.calcHist([image], [0], None, histSize, ranges)
hist2, bins = np.histogram(image, ranges_gap)

hist_img = draw_histo(hist1)
cv.imshow('hist1', hist_img)
#cv.imshow('hist2', draw_histo(hist2))
cv.waitKey(0)
cv.destroyAllWindows()