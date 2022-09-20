import numpy as np, cv2 as cv

image1 = cv.imread('./images/add1.jpg', cv.IMREAD_COLOR)
image2 = cv.imread('./images/add2.jpg', cv.IMREAD_COLOR)
if image1 is None or image2 is None: raise Exception("영상 파일 읽기 오류")
image3 = np.zeros(image1.shape, image1.dtype)

# 먼저 사용자에게 합쳐진 3개의 이미지를 보여주기 위해, 가로로(cv coord 기준 y축)으로 합쳐준다.
result = np.concatenate((image1, image3, image2), axis=1)

bar1 = 'image1'
bar2 = 'image2'

title = 'dst'

def OnChange(value):
    global image1, image2, image3, title, result
    # 여러 개의 OnChange 함수를 만들어서 사용하려고 하였으나, 결국 alpha, beta 값을 가져와야 하므로, 단일 함수로 작성하였음.
    alpha = cv.getTrackbarPos(bar1, title) / 100.0
    beta = cv.getTrackbarPos(bar2, title) / 100.0
    #print(alpha, beta)

    # 사용자가 조절한 alpha, beta 값을 기반으로 가중합을 하는 함수를 사용하여, 원하는 결과를 도출하였음.
    image3 = cv.addWeighted(image1, alpha, image2, beta, gamma=0.0)  
    # 다시 사용자에게 보여주기 위해, 원본, 결과 이미지를 다시 합쳤음.
    result = np.concatenate((image1, image3, image2), axis=1)

    #cv.imshow("test", image3)
    cv.imshow(title, result)


#cv.imshow("test", image3)
cv.imshow(title, result)

cv.createTrackbar(bar1, title, 0, 100, OnChange)
cv.createTrackbar(bar2, title, 0, 100, OnChange)

cv.waitKey(0)
cv.destroyAllWindows()