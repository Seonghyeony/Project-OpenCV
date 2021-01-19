import sys
import numpy as np
import cv2


src = cv2.imread('Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# 그레이스케일 영상의 히스토그램 평활화
dst = cv2.equalizeHist(src)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

# 컬러 영상의 히스토그램 평활화
src = cv2.imread('field.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

# 컬러 영상 히스토그램 평활화. 따로 분해 뒤 merge.
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
planes = cv2.split(src_ycrcb)

# 밝기 성분에 대해서만 히스토그램 평활화 수행
planes[0] = cv2.equalizeHist(planes[0])

dst_ycrcb = cv2.merge(planes)
dst = cv2.cvtColor(dst_ycrcb, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', src)
cv2.imshow('dst', dst)  # imshow는 컬러영상의 경우 기본적으로 BGR로 인식을 한다.
cv2.waitKey()

cv2.destroyAllWindows()
