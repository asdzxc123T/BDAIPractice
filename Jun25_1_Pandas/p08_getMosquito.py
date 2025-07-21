# 2016 ~ 2024
# 5/1 ~ 10/31
# 날짜, 집, 물가, 공원

from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

f = open("C:/ljw/mosquito.csv", "w", encoding="utf-8")
hc = HTTPConnection("openapi.seoul.go.kr", 8088)
for year in range(2016, 2025):
    for month in range(5, 11):
        for day in range(1, 32):
            hc.request("GET", "/575a4655496b636839386f58586542/xml/MosquitoStatus/1/5/%d-%02d-%02d" % (year, month, day)) 
            resBody = hc.getresponse().read()
            
            lnpsData = fromstring(resBody)
            for l in lnpsData.iter("row"):
                if l.find("MOSQUITO_DATE").text:
                    f.write(l.find("MOSQUITO_DATE").text + ",")
                    f.write(l.find("MOSQUITO_VALUE_WATER").text + ",")
                    f.write(l.find("MOSQUITO_VALUE_HOUSE").text + ",")
                    f.write(l.find("MOSQUITO_VALUE_PARK").text + "\n")
            print(year, month, day)
hc.close()
f.close()