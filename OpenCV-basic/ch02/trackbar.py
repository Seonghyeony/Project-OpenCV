import numpy as np
import cv2

# 트랙바: OpenCV에서 제공하는 유일한 그래픽 사용자 인터페이스

def on_level_changed(pos):
    global img

    level = pos * 16
    # 포화연산이라고 한다.
    # if level >= 255:
    #     level = 255
    level = np.clip(level, 0, 255) # 최소는 0 최대는 255로.

    img[:, :] = level
    cv2.imshow('image', img)

img = np.zeros((480, 640), np.uint8)

cv2.namedWindow('image')
cv2.imshow('image', img)
cv2.createTrackbar('level', 'image', 0, 16, on_level_changed)
cv2.waitKey()

cv2.destroyAllWindows()
