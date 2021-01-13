import sys
import cv2

# 카메라 열기
# cap = cv2.VideoCapture(0)
# cap.open(0)

# 동영상 열기
cap = cv2.VideoCapture('video1.mp4')

if not cap.isOpened():
    print('camera open failed!')
    sys.exit()

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(w, h)

# set으로 영상 크기 설정 가능.
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# 카메라로부터 한 프레임씩 계속 받아오는 작업.(무한 루프)
while True:
    # read()함수의 리턴 값이 2개 retval, image 이다.
    # retval: 성공하면 True, 실패하면 False.
    # image = 현재 프레임(numpy.ndarray)
    ret, frame = cap.read()

    if not ret:
        break

    inversed = ~frame  # 반전
    # 여기에 frame이라는 정지 영상을 처리하는 코드를 작성 가능.
    edge = cv2.Canny(frame, 50, 150)

    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)
    cv2.imshow('inversed', inversed)
    if cv2.waitKey(20) == 27:   # ESC
        break

cap.release()
cv2.destroyAllWindows()