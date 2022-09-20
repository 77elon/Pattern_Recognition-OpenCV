import cv2 as cv, numpy as np

BGR = cv.imread('./images/color_edge.jpg', cv.IMREAD_COLOR)

white = np.array([255, 255, 255], np.uint8)
CMY = white - BGR
CMY_split = cv.split(CMY)

black = cv.min(CMY_split[0], cv.min(CMY_split[1], CMY_split[2]))
Yellow, Magenta, Cyan = CMY_split - black

titles = ['black', 'Yellow', 'Magenta', 'Cyan']

[cv.imshow(t, eval(t)) for t in titles]
cv.waitKey(0)