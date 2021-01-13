import sys
import cv2

# 마스크 영상을 이용한 영상 합성
src = cv2.imread('airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('field.bmp', cv2.IMREAD_COLOR)

if src is None or mask is None or dst is None:
    print('Image load failed!')
    sys.exit()

'''
src, mask, dst = 사이즈 같아야 함.
src, dst = 타입이 같아야 함.
mask는 무조건 grayscale 이어야 함.
'''
# cv2.copyTo(src, mask, dst)

dst[mask > 0] = src[mask > 0]   # boolean 값. 이건 참조 형태.

# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()

'''------------------------------------------------------------------------------------'''
# 4채널 중 알파 채널을 마스크 영상으로 이용
src = cv2.imread('opencv-logo-white.png', cv2.IMREAD_UNCHANGED)    # UNCHANGED를 써야함. 4채널
mask = src[:, :, -1]
src = src[:, :, :3]
dst = cv2.imread('field.bmp', cv2.IMREAD_COLOR)

h, w = src.shape[:2]

# dst의 일부분을 잘라와서 공유한다.
crop = dst[10:h+10, 10:w+10]

cv2.copyTo(src, mask, crop)

# dst[mask > 0] = src[mask > 0]   # boolean 값. 이건 참조 형태.

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()
