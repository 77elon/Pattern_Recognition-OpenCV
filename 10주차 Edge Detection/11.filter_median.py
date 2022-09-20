import numpy as np, cv2 as cv

img = cv.imread('./images/median2.jpg')

def salt_pepper_noise(n):
    global img
    h, w = img.shape[:2]
    x, y = np.random.randint(0, h, n), np.random.randint(0, w, n)
    #print(y, x)
    noise = img.copy()
    # 전체 데이터를 접근하는 이중 반복문은 필요 없음.
    #for i in h:
        #for j in w:
    #print(list(zip(x, y)))
    # iteration once...
    for x, y in list(zip(x, y)):
        #print(x, y)
        if np.random.rand() < 0.5:
            #print('Execute1')
            noise[x, y] = 0   
        else:
            #print('Execute2')
            noise[x, y] = 255
    return noise


noise = salt_pepper_noise(500)
med_img = cv.medianBlur(noise, 5)


cv.imshow('image', img)
cv.imshow('noise', noise)
cv.imshow('med_img', med_img)

cv.waitKey()

