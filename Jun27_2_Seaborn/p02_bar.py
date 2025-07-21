import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from http.client import HTTPConnection
from json import loads
import pandas as pd
import seaborn as sns

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False

hc = HTTPConnection("openapi.seoul.go.kr:8088")
hc.request("GET", "/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/")
resBody = hc.getresponse().read()
print(resBody.decode())
hc.close()

dustData = loads(resBody)
dustData = dustData["RealtimeCityAir"]["row"]
dustDF = pd.DataFrame(dustData)

# sns.barplot(data=dustDF)
# sns.barplot(x="MSRSTE_NM", y="PM10", data=dustDF, palette="rainbow")

# 통계가 필요하면 알아서 통계내서(권역별 PM10평균)
# 검은선 : 신뢰구간 95%(기본)
# sns.barplot(x="MSRRGN_NM", y="PM10", data=dustDF, palette="rainbow")

# 검은선을 표준편차로
# sns.barplot(x="MSRRGN_NM", y="PM10", data=dustDF, palette="rainbow", errorbar="sd")

# 갯수
# 권역별 데이터 몇개씩
# sns.countplot(x="MSRRGN_NM", data=dustDF, palette="Pastel1")

# 권역별 데이터 몇개씩, 상태별 색깔 다르게
sns.countplot(x="MSRRGN_NM", data=dustDF, palette="Pastel1", hue="IDEX_NM")
plt.show()