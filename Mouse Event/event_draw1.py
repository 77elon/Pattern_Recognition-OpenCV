import numpy as np, cv2 as cv

def onMouse(event, x, y, flags, param=None):
    global title, pt, image

    if event == cv.EVENT_LBUTTONDOWN:
        pt = (x, y)
    elif event == cv.EVENT_LBUTTONUP:
        cv.rectangle(image, pt, (x, y), (255, 0, 0), 2)
        cv.imshow(title, image)
        pt = (-1, -1)
    elif event == cv.EVENT_RBUTTONDOWN:
        pt = (x, y)
    elif event == cv.EVENT_RBUTTONUP:
        dx, dy = pt[0] - x, pt[1] - y
        radius = int(np.sqrt(dx**2 + dy**2))
        cv.circle(image, pt, radius, (0, 0, 255), 2)
        cv.imshow(title, image)
        pt = (-1, -1)
image = np.full((300, 500, 3), (255, 255, 255), np.uint8)

pt = (-1, -1)
flag = -1
title = 'draw event'
cv.imshow(title, image)
cv.setMouseCallback(title, onMouse)
cv.waitKey(0)
cv.destroyAllWindows()