import numpy as np, cv2 as cv

angle = 20* np.pi / 180

rot_mat = np.array([[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]], dtype=np.float32)

pts1 = np.array(((250, 30), (400, 70), (350, 250), (150, 200)), dtype=np.float32)
pts2 = cv.gemm(pts1, rot_mat, 1, None, 1, flags=cv.GEMM_2_T)

for i, (pt1, pt2) in enumerate(zip(pts1, pts2)):
    print('pts[{}] = {}, pst2[{}] = {}'. format(i, pt1, i, pt2))



image = np.full((400, 500, 3), 255, dtype=np.uint8)
cv.polylines(image, [np.int32(pts1)], True, (0, 255, 0), 2)
cv.polylines(image, [np.int32(pts2)], True, (255, 0, 0), 3)


image1 = np.full((400, 500, 3), 255, dtype=np.uint8)
cv.polylines(image1, [np.int32(pts1)], True, (0, 255, 0), 2)

gray = cv.cvtColor(image1, cv.COLOR_BGR2GRAY)
res, thr = cv.threshold(gray, 127, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
contours, _ = cv.findContours(thr, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cnt = contours[1]

area = cv.contourArea(cnt)
x, y, w, h = cv.boundingRect(cnt)
rect_area = w * h
extend = float(area) / rect_area
print(extend)
tx = -(x + w / 2)
ty = -(y + h / 2)
rx = -tx
ry = -ty

#x2 = ((x1 - x0) * cos(a)) - ((y1 - y0) * sin(a)) + x0;
#y2 = ((x1 - x0) * sin(a)) + ((y1 - y0) * cos(a)) + y0;
#x0, y0 is base axis
rot_mat_param = np.array([[rx*np.cos(angle), -ry*np.sin(angle)], [rx*np.sin(angle), ry*np.cos(angle)]], dtype=np.float32)
pts3 = cv.gemm(pts1, rot_mat_param, 1, None, 1, flags=cv.GEMM_2_T) 
print(pts3)
cv.polylines(image1, [np.int32(pts3)], True, (255, 0, 0), 3)

# create the translation matrix using tx and ty, it is a NumPy array 
translation_matrix = np.array([
    [1, 0, tx],
    [0, 1, ty]
], dtype=np.float32)
rotated_matrix = cv.getRotationMatrix2D(center=(-tx, -ty), angle=45, scale=1)
print(rotated_matrix)

rotated_image = cv.warpAffine(src=image1, M=rotated_matrix, dsize=(image1.shape[1], image1.shape[0]))


cv.imshow('image', image)
cv.imshow('image1', image1)
cv.imshow('rotated_image', rotated_image)

cv.waitKey(0)
cv.destroyAllWindows()