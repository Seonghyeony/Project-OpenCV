import numpy as np
import cv2

# 그리기 알고리즘은 영상의 픽셀 값 자체를 변경하므로 복사본으로 작업.s

img = np.full((400, 400, 3), 255, np.uint8)

# 선 그리기
cv2.line(img, (50, 50), (200, 50), (0, 0, 255), 5)
cv2.line(img, (50, 60), (150, 160), (0, 0, 128))

# 꼭짓점 하나와 Width, Height를 준 것.
cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 2)
# 대각선의 꼭짓점
cv2.rectangle(img, (70, 220), (180, 280), (0, 128, 0), -1)  # -1을 지정하면 내부를 채움.

cv2.circle(img, (300, 100), 30, (255, 255, 0), -1, cv2.LINE_AA) # cv2.LINE_AA: 좀 더 자연스럽게 표현한다.
cv2.circle(img, (300, 100), 60, (255, 0, 0), 3, cv2.LINE_AA)

# 다각형
pts = np.array([[250, 200], [300, 200], [350, 300], [250, 300]])
cv2.polylines(img, [pts], True, (255, 0, 255), 2, cv2.LINE_AA)

# 문자열 출력, putText: 한글 지원 x
text = 'Hello! My name is SH.Lim.'
cv2.putText(img, text, (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 
                (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()

