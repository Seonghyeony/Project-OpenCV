import sys
import numpy as np
import cv2


# 그레이스케일 영상 불러오기
# src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE) # uint8
src = cv2.imread('lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.add(src, (100, 100, 100, 0))
# dst = np.clip(src + 100., 0, 255).astype(np.uint8) # src: ndarray type, 255보다 커지면 0부터 셋팅 한다.

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
