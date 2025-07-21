# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/json/CardSubwayPayFree/1/630/201501

# 년월, 노선, 역, 찍고타, 안찍고타, 찍고내린, 안찍고내린 -> csv
from json import loads
from http.client import HTTPConnection
import pandas as pd

f = open("C:/ljw/cspf.csv", "a", encoding="utf-8")
hc = HTTPConnection("openapi.seoul.go.kr", 8088)
for y in range(2015, 2025):
    for m in range(1, 13):
        when = "%d%02d" % (y, m)
        hc.request("GET", "/575a4655496b636839386f58586542/json/CardSubwayPayFree/1/630/" + when)
        resBody = hc.getresponse().read()
        for d in loads(resBody)["CardSubwayPayFree"]["row"]:
            f.write("%s, " % d["USE_MM"])
            f.write("%s, " % d["SBWY_ROUT_LN_NM"].replace(",", ""))
            f.write("%s, " % d["STTN"].replace(",", ""))
            f.write("%.0f, " % d["RMIO_GTON_NOPE"])
            f.write("%.0f, " % d["FREECHRG_GTON_NOPE"])
            f.write("%.0f, " % d["RMIO_GTOFF_NOPE"])
            f.write("%.0f\n" % d["FREECHRG_GTOFF_NOPE"])
        print(when)
hc.close()

