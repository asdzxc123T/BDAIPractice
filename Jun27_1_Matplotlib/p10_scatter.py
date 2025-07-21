import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False

df = pd.read_csv("C:/Kwon/cspf.csv", 
        names=["언제", "노선", "역", "찍고타", "그냥타", "찍고내려", "그냥내려"])
df = df.groupby("노선")[["찍고타", "그냥타", "찍고내려", "그냥내려"]].mean()

yData1 = df["찍고타"].to_numpy()
yData2 = df["그냥타"].to_numpy()
yData3 = df["찍고내려"].to_numpy()
yData4 = df["그냥내려"].to_numpy()
xLabel = df.index.to_numpy()
xData = np.arange(len(xLabel))

# 산점도
#       꺾은선그래프인데 선 안이은거 - x
#       분포, x/y관계
# plt.scatter(yData1, yData3)
# plt.scatter(yData1, yData2)

yData5 = (yData2 + yData4) / 1000

# 많이 찍고 타면, 많이 찍고 내리는데
# 그냥시리즈랑은 그닥 상관없는
plt.scatter(yData1, yData3, color="green", alpha=0.3, s=yData5)
plt.show()