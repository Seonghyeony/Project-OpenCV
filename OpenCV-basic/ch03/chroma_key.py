import sys
import numpy as np
import cv2


# 녹색 배경 동영상
cap1 = cv2.VideoCapture('woman.mp4')

# 내 장치 카메라
# cap1 = cv2.VideoCapture(0)

if not cap1.isOpened():
    print('video open failed!')
    sys.exit()

# 비오는 배경 동영상
cap2 = cv2.VideoCapture('raining.mp4')

if not cap2.isOpened():
    print('video open failed!')
    sys.exit()

# 두 동영상의 크기, FPS는 같다고 가정
w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))

frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))  # 총 프레임 수
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

print('w x h: {} x {}'.format(w, h))
print('frame_cnt1:', frame_cnt1)
print('frame_cnt2:', frame_cnt2)

fps = cap1.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps) # 두개의 프레임 사이에 들어갈 시간 간격.

# 출력 동영상 객체 생성
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

# 합성 여부 플래그
do_composit = False # true 면 합성을 한다.

# 전체 동영상 재생
while True:
    ret1, frame1 = cap1.read()

    if not ret1:
        break
    
    # do_composit 플래그가 True일 때에만 합성
    if do_composit:
        ret2, frame2 = cap2.read()

        if not ret2:
            break
        
        # 장치 카메라를 사용할 경우 영상 크기 변경.
        frame2 = cv2.resize(frame2, (w, h))

        # HSV 색 공간에서 녹색 영역을 검출하여 합성
        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (50, 150, 0), (70, 255, 255))
        # copyTo(): 마스크 연산; 흰색 영역에 대해서만 연산.
        cv2.copyTo(frame2, mask, frame1)

    out.write(frame1)

    cv2.imshow('frame', frame1)
    key = cv2.waitKey(delay) # 41ms 기다리고 다음 영상으로.

    # 스페이스바를 누르면 do_composit 플래그를 변경
    if key == ord(' '):
        do_composit = not do_composit
    elif key == 27:     # ESC를 누르면 종료.
        break

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()
