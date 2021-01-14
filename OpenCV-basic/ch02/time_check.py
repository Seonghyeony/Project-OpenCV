import sys
import numpy as np
import cv2
import time

# 좀 더 빠르게 동작할 수 있는 방법이 무엇이 있을까 라는 고민을 계속 하는 것이 정말 중요하다!
# 보통 30ms 정도가 빠르다고 할 수 있다.

img = cv2.imread('hongkong.jpg')

if img is None:
    print('Image load failed!')
    sys.exit()

tm = cv2.TickMeter()
tm.start()
t1 = time.time()

edge = cv2.Canny(img, 50, 150)

t2 = time.time()
tm.stop()
ms = tm.getTimeMilli()

# 파이썬 time 라이브러리를 활용해도 됌.
result = t2 - t1
# 평균적인 시간측정을 해보는 것도 좋다.
print('Elapsed time: {}ms.'.format(ms))

