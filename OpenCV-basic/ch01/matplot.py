import matplotlib.pyplot as plt
import cv2


# 컬러 영상 출력
# cv2.imread() 함수로 불러온 영상의 색상 정보는 BGR 순이다.
imgBGR = cv2.imread('cat.bmp')
# 컬러 영상의 색상 정보가 RGB 순서이어야 하기 때문에
# cvtColor 로 BGR -> RGB 순서로 바꿈.
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

plt.axis('off') # axis('off'): 눈금선 제거.
plt.imshow(imgRGB)
plt.show()

# 그레이스케일 영상 출력 2차원.
imgGray = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(imgGray, cmap='gray')    # 그레이스케일은 cmap='gray' 설정을 꼭 해야함.
plt.show()

# 두 개의 영상을 함께 출력
# subplot(121) 121: 1행 2열로 나누고 1 번째에 표시
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray')
plt.show()
