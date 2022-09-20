import numpy as np, cv2 as cv

image = cv.imread('./images/abs_test2.jpg')

bar_name = 'Brightness'
title = 'Mouse Trackbar Event'

def onChange(value):
    global image, title

    add_value = np.uint8(value - image[0][0][:3])
    #print(int(add_value))

    image += add_value
    cv.imshow(title, image)
    #cv.imshow('onChange', image)


def onMouseFunc(event, x, y, flags, param=None):
    global image, bar_name

    if event == cv.EVENT_RBUTTONDOWN:
        if(cv.mean(image[0][0][:3]) < 246):
            image = image + 10
        cv.setTrackbarPos(bar_name, title, image[0][0][2])
        cv.imshow(title, image)
    elif event == cv.EVENT_LBUTTONDOWN:
        if image[0][0] >= 10:
            image = image - 10
        cv.setTrackbarPos(bar_name, title, image[0][0][2])
        cv.imshow(title, image)


cv.imshow(title, image)

cv.createTrackbar(bar_name, title, image[0][0][2], 255, onChange)
cv.setMouseCallback(title, onMouseFunc)
cv.waitKey(0)
cv.destroyAllWindows()