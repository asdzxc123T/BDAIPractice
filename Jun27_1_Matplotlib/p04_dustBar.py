# 실시간 미세먼지
from json import loads
from http.client import HTTPConnection
import pandas as pd

hc = HTTPConnection("openapi.seoul.go.kr", 8088)
hc.request("GET", "/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/")
resBody = hc.getresponse().read()
hc.close()

dustData = loads(resBody)
dustData = dustData["RealtimeCityAir"]["row"]
dusts = pd.DataFrame(dustData)

dusts["MSRDT"] = dusts["MSRDT"].apply(lambda t: "%02d/%02d %02d시" % (int(t[4:6]), int(t[6:8]), int(t[8:10])))
print(dusts)

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False

pm10 = dusts["PM10"].to_numpy()
pm25 = dusts["PM25"].to_numpy()
msrste_nm_label = dusts["MSRSTE_NM"].to_numpy()
msrste_nm_data = np.arange(len(msrste_nm_label))

plt.bar(msrste_nm_data, pm10, color="red")
plt.bar(msrste_nm_data, pm25, color="blue", bottom=pm10)
plt.title("서울시 구별 미세먼지")
plt.xticks(msrste_nm_data, msrste_nm_label)
plt.show()