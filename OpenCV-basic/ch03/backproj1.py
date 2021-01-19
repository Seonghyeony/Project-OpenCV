import sys
import numpy as np
import cv2


# 입력 영상에서 ROI를 지정하고, 히스토그램 계산

src = cv2.imread('cropland.png')

if src is None:
    print('Image load failed!')
    sys.exit()

# selectROI(): 마우스를 이용하여 어떤 영역을 드래그해서 선택 가능.
x, y, w, h = cv2.selectROI(src)

src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
# crop은 사용자가 선택한 사각형 영역의 부분 영상.
crop = src_ycrcb[y:y+h, x:x+w]

# 0번 채널; Y: 밝기
channels = [1, 2]   # 0번 채널은 사용하지 않는다. 색상 정보만 사용.
cr_bins = 128       # 단순화; 256을 써도 달라지진 않는다.
cb_bins = 128
histSize = [cr_bins, cb_bins]
cr_range = [0, 256]
cb_range = [0, 256]
ranges = cr_range + cb_range

hist = cv2.calcHist([crop], channels, None, histSize, ranges)
hist_norm = cv2.normalize(cv2.log(hist+1), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# 입력 영상 전체에 대해 히스토그램 역투영

# 위에서 계산한 hist 값을 이용해서 
# calcBackProject()로 내가 원하는 영역만 골라낼 수 있다. 
backproj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1)
dst = cv2.copyTo(src, backproj)

cv2.imshow('backproj', backproj)
cv2.imshow('hist_norm', hist_norm)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
