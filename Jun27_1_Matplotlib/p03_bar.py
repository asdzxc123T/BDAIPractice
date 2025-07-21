import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False

# 막대그래프 : 항목간 절대적인 크기 비교 -> x축이 숫자일 필요는 없음(width 조절하려면 숫자여야)
yData = np.array([12, 10, 5, 22, 8])
yData2 = np.array([22, 33, 11, 7, 3])
xLabel = ["ㄱ", "ㄴ", "ㄷ", "ㄹ", "ㅁ"]
xData = np.arange(len(xLabel))

# 기본
# plt.bar(xData, yData)
# plt.show()

# 기본 2
# plt.bar(xData, yData)
# plt.xticks(xData, xLabel)
# plt.show()

# 디자인
# plt.bar(xData, yData,
#         color="#ff0000", width=1, # 단위 : x값
#         edgecolor="#0000ff", linewidth=5 # 단위: px
#         )
# colorss = ["red", "green", "blue", "#43a047", "#ff035a"]
# plt.bar(xData, yData,
#         color=colorss, width=1,
#         edgecolor="#0000ff", linewidth=5
#         )
# plt.show()

# y값 여러개(옆에 나오게) - 자체 기능은 없음
# plt.bar(xData, yData, align="edge", width=0.3, color="red") # 첫 데이터 0, 12
# plt.bar(xData - 0.3, yData2, align="edge", width=0.3, color="blue") # 첫 데이터 -0.3, 22
# plt.show()

# y값 여러개(누적합)
plt.bar(xData, yData)
plt.bar(xData, yData2, bottom=yData)
plt.xticks(xData, xLabel)
plt.show()
