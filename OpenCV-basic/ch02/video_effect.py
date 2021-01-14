import sys
import numpy as np
import cv2

'''
과제: 동영상 전환 이펙트
1. 두 동영상 클립 사이에 추가되는 애니메이션 효과
2. fade-in, fade-out, dissolve, 밀기, 확대 등

구현할 기능
1. 두 개의 동영상 동시 열기
2. 첫 번째 동영상의 마지막 N개 프레임과 두 번째 동영상의 처음 N개 프레임을 합성
3. 합성된 영상을 동영상으로 저장하기.
'''

# 두 개의 동영상을 열어서 cap1, cap2로 지정
cap1 = cv2.VideoCapture('video1.mp4')
cap2 = cv2.VideoCapture('video2.mp4')

if not cap1.isOpened() or not cap2.isOpened():
    print('video open failed!')
    sys.exit()

# 두 동영상의 크기, FPS는 같다고 가정함

# 동영상의 전체 프레임 수
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv2.CAP_PROP_FPS)
# 첫 번째 동영상의 끝 부분 2초, 두 번째 동영상의 앞 부분 2초를 합성하려고 함.
effect_frames = int(fps * 2) # 48 프레임

print('frame_cnt1:', frame_cnt1)
print('frame_cnt2:', frame_cnt2)
print('FPS:', fps)

delay = int(1000 / fps) # 두 프레임 사이의 시간 간격

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# 출력 동영상 객체 생성
out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

# 1번 동영상
for i in range(frame_cnt1 - effect_frames):
    ret1, frame1 = cap1.read()
    if not ret1:
        break

    out.write(frame1)

    cv2.imshow('frame', frame1)
    cv2.waitKey(delay)

# 합성하는 구간
for i in range(effect_frames):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    # 합성
    dx = int(w * i / effect_frames) # 26.7777..

    '''
    <밀어내기 기능>
    frame = np.zeros((h, w, 3), dtype=np.uint8)
    frame[:, 0:dx] = frame2[:, 0:dx]
    frame[:, dx:w] = frame1[:, dx:w]
    '''

    # <dissolve 기능>
    alpha = 1.0 - i / effect_frames # 0-1 값. i가 0일 때 alpha 값이 1이 되어야 한다.
    frame = cv2.addWeighted(frame1, alpha, frame2, 1 - alpha, 0)

    out.write(frame)
    cv2.imshow('frame', frame)
    cv2.waitKey(delay)

# 2번 동영상
for i in range(effect_frames, frame_cnt2):
    ret2, frame2 = cap2.read()
    if not ret2:
        break

    out.write(frame2)

    cv2.imshow('frame', frame2)
    cv2.waitKey(delay)

# print('\noutput.avi file is successfully generated!')

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()
