import sys
import numpy as np
import cv2

# 이전 마우스 포인터부터 현재 마우스 포인터까지의 직선을 그린다.
oldx = oldy = -1

# 5개 파라미터는 필수다.
def on_mouse(event, x, y, flags, param):
    global img, oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print('EVENT_LBUTTONDOWN: {}, {}'.format(x, y))
    elif event == cv2.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP: {}, {}'.format(x, y))
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:  # flags로 들어오는 변수의 마지막 비트가 1로 들어와 있냐
            # print('EVENT_LBUTTONMOVE: {}, {}'.format(x, y))
            '''circle 로 하면 빠르게 움직일 경우 끊김 현상'''
            # cv2.circle(img, (x, y), 5, (0, 0, 255), -1) # -1은 내부로 채운 형태
            '''그래서 직선으로 그리면 끊김 현상이 없다.'''
            cv2.line(img, (oldx, oldy), (x, y), (0, 0, 255), 5, cv2.LINE_AA)
            cv2.imshow('image', img)
            oldx, oldy = x, y
    

img = np.ones((480, 640, 3), dtype=np.uint8) * 255

cv2.namedWindow('image')
cv2.imshow('image', img)
# 마우스 콜백 함수는 namedWindow 함수로 창이 띄어졌을 때
# 혹은 imshow가 호출된 이후에 등록해야 한다.
cv2.setMouseCallback('image', on_mouse)
cv2.waitKey()

cv2.destroyAllWindows()
