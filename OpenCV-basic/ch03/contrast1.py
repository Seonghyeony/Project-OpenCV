import sys
import numpy as np
import cv2

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

# 적절한 명암비라는 것은 상황에 따라 달라지는 것이므로 수식도 이에 해당한다.
# 그래서 알맞은 명암비와 함수를 상황에 따라 알맞는 것을 사용하자.
alpha = 0.5
dst = np.clip((1 + alpha) * src - 128 * alpha, 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
