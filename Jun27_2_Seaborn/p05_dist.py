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

# sns.histplot(x="PM10", data=dustDF) # 히스토그램
# sns.pairplot(data=dustDF) # 히스토그램 + scatter
# sns.violinplot(x="PM10", data=dustDF)
sns.violinplot(x="PM10", y="MSRRGN_NM", data=dustDF, hue="MSRRGN_NM", palette="pastel")
plt.show()
