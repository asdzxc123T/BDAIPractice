# DB -> 전처리 -> NumPy/Pandas + ML/DL

# -> 결과를 파일로 저장 -> 엑셀에서 불러서 그래프
# -> 결과를 JSON으로 주는 백엔드 작업 -> JS에서 불러서 그래프
# -> Python 시각화 라이브러리 Matplotlib

# pip install matplotlib

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

# matplotlib의 기본폰트에 한글 없음 -> 한글 있는 폰트로 바꾸자
# C:\Windows\Fonts 폴더에 가서
#   cmd - dir (폰트명x, 정식 파일명 확인)
#   그나마도 다 되진 않음
fontFile = "C:/Windows/Fonts/malgun.ttf" # 설치된 폰트파일 경로
fontName = fm.FontProperties(fname=fontFile, size=10).get_name() # 폰트이름
plt.rc("font", family=fontName) # matplotlib 기본폰트 바꾸기
plt.rcParams["axes.unicode_minus"] = False # - 안 깨지게

# matplotlb이 np.array를 대상으로
yData = np.array([12, 10, 5, 22, 8])
xData = [10, 20, 30, 40, 50] # 쌩 list -> np.array로 바꿔서 활용함

# 기본
# plt.plot(yData) # plt에 이래저래 세팅
# plt.show() # 그래프 띄우기

# x, y
# plt.plot(xData, yData)
# plt.show() 

# 축
# plt.plot(xData, yData)
# plt.xlabel("xxx")
# plt.ylabel("와이")
# plt.axis([0, 300, -50, 200]) # x최소, x최대, y최소, y최대
# plt.show()

# 제목
# d = {"fontsize": 20, "fontweight": "bold", "color": "#FF0000"}
# plt.plot(xData, yData)
# plt.title("제목", loc="left")
# plt.title("제목2")
# plt.title("제목3", loc="right", fontdict=d)
# plt.show()

# 선
# matplotlib cheat sheet 검색
# plt.plot(xData, yData, "r:X")
# plt.plot(xData, yData, color="#43A047", linestyle="-.", marker="P", linewidth=7)
# plt.show()

# 격자
plt.plot(xData, yData)
plt.grid(axis="x", color="red", linestyle=':')
plt.show()