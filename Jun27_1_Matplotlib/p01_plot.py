import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False

yData = np.array([12, 10, 5, 22, 8])
xData = [10, 20, 30, 40, 50]

# 꺾은선그래프
# xData가 변화할 때 yData가 어떻게 변화하나 추이 보려고
# -> xData도 숫자여야, yData는 당연히 숫자고

# 눈금
# plt.plot(xData, yData)
# plt.xticks(xData, ["ㅋ", "ㅎ", "ㅇ", "ㅡ", "ㅠ"])
# # plt.yticks(yData, ["q", "w", "e", "r", "t"])
# plt.yticks(np.arange(0, 23, 5), ["q", "w", "e", "r", "t"])
# plt.tick_params("x", direction="inout", length=20, pad=10)
# plt.tick_params("y", color="#FF0000", labelcolor="#0000ff", labelsize=20)
# plt.show()

# 선 여러개
# yData2 = [55, 10, 50, 12, 6]
# plt.plot(xData, yData)
# plt.plot(xData, yData2, "r-*")
# plt.legend(["어제거", "지금 만든 거"])
# plt.show()

# 선 여러개2(y축을 나눠서)
yData2 = [10000, 9090, 6054, 4238, 7860]

_, sub1Conf = plt.subplots()
p1 = sub1Conf.plot(xData, yData)
sub1Conf.set_xlabel("엑스축")
sub1Conf.set_ylabel("어제거")

sub2Conf = sub1Conf.twinx()
p2 = sub2Conf.plot(xData, yData2, "r")
sub2Conf.set_ylabel("지금거")

sub1Conf.legend(p1 + p2, ["어제거", "지금 만든거"])
plt.show()
