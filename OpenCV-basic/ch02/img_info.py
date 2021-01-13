import sys
import cv2

# 영상 불러오기
img1 = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)

if img1 is None or img2 is None:
    print('Image load failed!')
    sys.exit()

# 영상의 속성 참조
print(type(img1))
print(img1.shape)
print(img2.shape)
print(img1.dtype)
print(img2.dtype)

# 영상의 크기 참조
h, w = img1.shape[:2]
print('img1: w x h = {} x {}'.format(w, h))

h, w = img2.shape[:2]
print('img2: w x h = {} x {}'.format(w, h))

h, w = img1.shape
print('w x h = {} x {}'.format(w, h))

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()
    
# 픽셀 값 접근
# x = 20
# y = 10
# p1 = img1[y][x]
# print(p1)
# img1[y, x] = 0

# p2 = img2[y][x]
# print(p2)
# img2[y, x] = (0, 0, 255)

# 영상의 픽셀 값 참조 
'''
# - 이렇게는 엄청나게 느리므로 하면 안됌.
# - 파이썬에서는 이것이 너무 느려서 안됌.
for y in range(h):
    for x in range(w):
        img1[y, x] = 0
        img2[y, x] = (0, 255, 255)
'''

# 요런식으로 모든 픽셀 값을 한꺼번에 접근하는 것을 고민 해야함.
img1[:, :] = 0
img2[:, :] = (0, 255, 255)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.waitKey()

cv2.destroyAllWindows()
