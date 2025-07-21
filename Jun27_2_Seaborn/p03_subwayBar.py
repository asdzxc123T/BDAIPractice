from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import seaborn as sns

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False

df = pd.read_csv(
    "C:/Kwon/subway.csv", names=["년", "월", "일", "노선", "역", "탄", "내린"]
)
df["이용객수"] = df["탄"] + df["내린"]

# 노선별 이용객수(탄+내린) 평균 막대그래프
# sns.barplot(x="노선", y="이용객수", data=df, palette="terrain", hue="노선")

# 요일별 이용객수(탄+내린) 평균 막대그래프
def getYoil(stationData):
    when = "%d%02d%02d" % (stationData["년"], stationData["월"], stationData["일"])
    when = datetime.strptime(when, "%Y%m%d")
    return datetime.strftime(when, "%a")

df["요일"] = df.apply(getYoil, axis=1)

sns.barplot(x="요일", y="이용객수", data=df, palette="cool", hue="요일")
plt.show()
