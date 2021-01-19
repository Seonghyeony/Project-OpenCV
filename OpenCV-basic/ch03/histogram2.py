import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2

# matplot 라이브러리를 사용하지 않고
# OpenCV 함수만을 이용해서 히스토그램을 화면에 출력할 수 있다.
def getGrayHistImage(hist):
    imgHist = np.full((100, 256), 255, dtype=np.uint8)  # h: 100, w: 256으로 제한.

    histMax = np.max(hist)
    for x in range(256):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax))    # 히스토그램 길이가 100px 위로는 올라가지 않도록 제한.
        cv2.line(imgHist, pt1, pt2, 0)  # 그리는 함수.

    return imgHist


src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

hist = cv2.calcHist([src], [0], None, [256], [0, 256])
histImg = getGrayHistImage(hist)

cv2.imshow('src', src)
cv2.imshow('histImg', histImg)
cv2.waitKey()

cv2.destroyAllWindows()
