import numpy as np, cv2 as cv

#diff Blending(force pixel adding) and synthesis(composite)
image1 = cv.imread('./images/add1.jpg')
image2 = cv.imread('./images/add2.jpg')

if image1 is None or image2 is None: raise Exception('영상 파일 읽기 오류')

# For Blending
alpha, beta = 0.6, 0.7
# Exceed Problem 
# pixel[x, y] > 255
add_img1 = cv.add(image1, image2)
# Blending Ratio
add_img2 = cv.add(image1 * alpha, image2 * beta)
# operating numpy's modulo or Normalize
add_img2 = np.clip(add_img2, 0, 255).astype('uint8')
add_img3 = cv.addWeighted(image1, alpha, image2, beta, gamma=0)

titles = ['image1', 'image2', 'add_img1', 'add_img2', 'add_img3']
for t in titles:
    cv.imshow(t, eval(t))
cv.waitKey(0)
cv.destroyAllWindows()