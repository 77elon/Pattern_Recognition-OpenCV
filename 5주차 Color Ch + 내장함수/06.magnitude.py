import numpy as np, cv2

x = np.array((1, 2, 3, 5, 10), np.float32)
y = np.array((2, 5, 7, 2, 9), np.float32)

# Gradient 값을 구할 때 사용, 배열의 크기 계산에 사용.
mag = cv2.magnitude(x, y)
# x, y 좌표 기반의 회전 각도 계산. angle is radian
ang = cv2.phase(x, y)

p_mag, p_ang = cv2.cartToPolar(x, y)
x2, y2 = cv2.polarToCart(p_mag, p_ang)

print("[x]: %s, 원소: %s" %(x.shape, x))
print("[mag]: %s, 원소: %s" %(mag.shape, mag))

print("열 벡터를 1행에 출력하기")
print("[m_mag]: ", mag.T)
print("[p_mag]: ", np.ravel(p_mag))
print("[p_ang]: ", np.ravel(p_ang))
print("[x_mat2] = ", x2.flatten())
print("[y_mat2] = ", y2.flatten())