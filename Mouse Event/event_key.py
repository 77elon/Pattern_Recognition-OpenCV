import numpy as np, cv2 as cv

switch_case ={
    ord('a'): 'a키 입력',
    ord('b'): 'b키 입력'

}

image = np.ones((200, 300), dtype=np.float)

cv.namedWindow('keyboard event')
cv.imshow('keyboard event', image)

while True:
    key = cv.waitKeyEx(100)
    if key == 27: break

    try:
        result = switch_case[key]
        print(result)
    except KeyError:
        result = -1
