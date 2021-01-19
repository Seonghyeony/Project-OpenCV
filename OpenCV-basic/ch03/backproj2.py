import sys
import numpy as np
import cv2


# CrCb 살색 히스토그램 구하기
ref = cv2.imread('kids1.png', cv2.IMREAD_COLOR)
mask = cv2.imread('kids1_mask.bmp', cv2.IMREAD_GRAYSCALE)

if ref is None or mask is None:
    print('Image load failed!')
    sys.exit()

ref_ycrcb = cv2.cvtColor(ref, cv2.COLOR_BGR2YCrCb)

channels = [1, 2]
ranges = [0, 256, 0, 256]

# calcHist()에서 mask 값을 입력하면 이 mask 영역에서의 히스토그램을 구한다.
hist = cv2.calcHist([ref_ycrcb], channels, mask, [128, 128], ranges)

# cv2.log 스케일로 만들어 주는 것이 좋다. 작은 것들은 0에 가깝게 나오고 큰 것들만 밝게 나오기 때문.
# cv2.log(hist + 1): +1 을 하는 이유는 log(hist) 값이 0일 수 있기 때문.
# grayscale로 변환: cv2.CV_8U
hist_norm = cv2.normalize(cv2.log(hist + 1), None, 0, 255, 
                          cv2.NORM_MINMAX, cv2.CV_8U)

# 입력 영상에 히스토그램 역투영 적용
src = cv2.imread('kids2.png', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)

# 아까 계산한 hist를 이용하여.
backproj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1) # grayscale 영상이다.

cv2.imshow('src', src)
cv2.imshow('hist_norm', hist_norm)
cv2.imshow('backproj', backproj)
cv2.waitKey()
cv2.destroyAllWindows()
