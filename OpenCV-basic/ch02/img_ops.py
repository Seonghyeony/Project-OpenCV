import numpy as np
import cv2

# 새 영상 생성하기
img1 = np.empty((240, 320), dtype=np.uint8)     # grayscale image, 랜덤 값.
img2 = np.zeros((240, 320, 3), dtype=np.uint8)  # 모든 픽셀 0으로
img3 = np.ones((240, 320, 3), dtype=np.uint8) * 255
img4 = np.full((240, 320), 128, dtype=np.uint8) # 원하는 값으로.

# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
# cv2.imshow('img3', img3)
# cv2.imshow('img4', img4)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 영상 복사
img1 = cv2.imread('HappyFish.jpg')

img2 = img1         # = 는 참조 개념
img3 = img1.copy()  # .copy() 는 값 복사 개념

# img1[:, :] = (0, 255, 255)

# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
# cv2.imshow('img3', img3)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 부분 영상 추출
img1 = cv2.imread('HappyFish.jpg')

img2 = img1[40:120, 30:150]  # numpy.ndarray의 슬라이싱
img3 = img1[40:120, 30:150].copy()

# img2.fill(0)    # 특정 ROI를 지정해서 처리를 가능.
cv2.circle(img2, (50, 50), 20, (0, 0, 255), 2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()
