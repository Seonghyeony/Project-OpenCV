import sys
import cv2

print('Hello, OpenCV', cv2.__version__)

# imread의 디폴트 값은 cv2.IMREAD_COLOR
img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('Image load failed!')
    sys.exit()

cv2.imwrite('cat_gray.png', img)

# 창 띄우기
cv2.namedWindow('image') # flags=None = windowAutoSize
# 영상 출력하기
cv2.imshow('image', img) # uint8 1바이트를 사용하는 ndarray를 넘겨주어야 한다.

# 여기 waitKey() 라는 함수까지 와야 실제로 영상이 출력이 된다.
# 실질적으로는 여기서 영상이 출력됌.
while True:
    if cv2.waitKey() == ord('q'):
        break
# key = cv2.waitKey(2000)   # 키보드 입력을 기다리는 함수.
# print(key)

# 창 닫기
cv2.destroyWindow('image')
# cv2.destroyAllWindows()