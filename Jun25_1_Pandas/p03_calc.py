# 실시간 미세먼지 df
from json import loads
from http.client import HTTPConnection
import pandas as pd

hc = HTTPConnection("openapi.seoul.go.kr", 8088)
hc.request("GET", "/575a4655496b636839386f58586542/json/RealtimeCityAir/1/25/")
resBody = hc.getresponse().read()
hc.close()

dustData = loads(resBody)
dustData = dustData["RealtimeCityAir"]["row"]
dustDF = pd.DataFrame(dustData)
# print(dustDF)
# print(dustDF["PM10"] + dustDF["PM25"]) # 필드끼리 연산자 써서 연산 가능
dustDF["PM_SUM"] = dustDF["PM10"] + dustDF["PM25"]
print(dustDF)