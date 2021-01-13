import sys
import cv2


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

# cap.get() 이 Double형이라서 정수 값 만들기 위해 round
w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = cap.get(cv2.CAP_PROP_FPS) # 카메라마다 다름.
fps = 30

fourcc = cv2.VideoWriter_fourcc(*'DIVX') # *'DIVX' == 'D', 'I', 'V', 'X'
delay = round(1000 / fps) # 한 프레임과 그 다음 프레임의 시간 간격

out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

if not out.isOpened():
    print('File open failed!')
    cap.release()
    sys.exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break
    
    # inversed = ~frame
    edge = cv2.Canny(frame, 50, 150) # grayscale이다.
    # grayscale을 저장하려면 color로 변환을 해주어야 한다.
    edge_color = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

    out.write(edge_color)

    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)
    cv2.imshow('edge_color', edge_color)

    if cv2.waitKey(delay) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
