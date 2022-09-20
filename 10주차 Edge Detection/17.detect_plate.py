import numpy as np, cv2 as cv

while True: 
    no = int(input('차량 영상 번호(0: 종료): '))
    if no == 0: break

    fname = './images/test_car/{0:02d}.jpg'.format(no)
    image = cv.imread(fname)
    if image is None:
        print(str(no) + '번 영상파일이 없습니다.')
        continue

    mask = np.ones((5, 17), image.dtype)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray = cv.blur(gray, (5, 5))
    gray = cv.Sobel(gray, cv.CV_8U, 1, 0, 5)

    th_img = cv.threshold(gray, 120, 255, cv.THRESH_BINARY)[1]
    morph = cv.morphologyEx(th_img, cv.MORPH_CLOSE, kernel=mask, iterations=3)

    cv.imshow('image', image)
    cv.imshow('binary_image', th_img)
    cv.imshow('opening', morph)

    cv.waitKey()