import numpy as np, cv2 as cv

image1 = cv.imread('./images/bit_test.jpg', cv.IMREAD_COLOR)
logo = cv.imread('./images/logo.jpg', cv.IMREAD_COLOR)
if image1 is None or logo is None: raise Exception("영상 파일 읽기 오류")

# Black XOR Logo -> 로고 추출이 될 것으로 예상되지만... 실질적으로 복사된 로고의 마스크가 필요하므로 의미 없다.
logo_extract = np.zeros(logo.shape, logo.dtype)
logo_extract = cv.bitwise_xor(logo, logo_extract)

#가로에 들어갈 개수를 입력하시오.
y = int(input("가로에 들어갈 개수를 입력하시오. >> "))

#세로에 들어갈 개수를 입력하시오.
x = int(input("세로에 들어갈 개수를 입력하시오. >> "))

# 결국 원본 이미지에 사용자가 입력한 숫자의 로고가 입력되어야 하므로, 
# 입력된 숫자로 나눔으로, 로고의 타겟 해상도를 알아낼 수 있다.
dsize = image1.shape[1] / y , image1.shape[0] / x
dsize = np.array(dsize, dtype=np.uint8)
#print(dsize)

# 이미지 강제 축소
logo_extract = cv.resize(logo_extract, dsize)

#cv.imshow("test", logo_extract)
#cv.waitKey()

logo_tuple = logo_extract.copy()
# 로고 이미지를 반복문을 사용하여, 가로로 먼저 합치고, 세로로 합치는 과정이다.
for _ in range(y - 1):
    logo_tuple = cv.hconcat([logo_tuple, logo_extract])
logo_result = logo_tuple.copy()
#print(logo_result.shape, logo_tuple)
for _ in range(x - 1):
    logo_result = cv.vconcat([logo_result, logo_tuple])

# 매트릭스 연산을 위해... 반복된 로고 이미지의 크기를 맞춰준다.<- 절대적으로 실제 이미지 크기와 같은 비율의 이미지 복사가 진행될 수 없으므로... i.,e) 603 / 6 -> 100.5 소수점 단위의 해상도는 존재하지 못하므로...!
logo_result = cv.resize(logo_result, dsize=(image1.shape[1], image1.shape[0]))
#print(logo_result.shape, image1.shape)

# 이미지 병합을 위한 마스크 생성.
masks = cv.threshold(logo_result, 220, 255, cv.THRESH_BINARY)[1]
masks = cv.split(masks)
# 모든 컬러 채널이 가지는 데이터를 마스크와 병합함.
lg_pass_mask = cv.bitwise_or(masks[0], masks[1])
lg_pass_mask = cv.bitwise_or(lg_pass_mask, masks[2])

result = cv.copyTo(logo_result, lg_pass_mask, image1)

#cv.imshow("test", logo_result)
#cv.imshow("image", image1)
cv.imshow("image", result)
cv.waitKey()
cv.destroyAllWindows()
