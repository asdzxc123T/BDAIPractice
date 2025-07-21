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
print(dusts)