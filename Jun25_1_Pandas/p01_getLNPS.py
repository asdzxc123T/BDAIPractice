# data.seoul.go.kr
# 생필품으로 검색
# -> 서울시 생필품 농수축산물 가격...
# -> Open API
# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/xml/ListNecessariesPricesService/1/10
# csv로

# M_NAME, A_NAME, A_PRICE, P_DATE, M_TYPE_NAME, M_GU_NAME

from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

f = open("C:/ljw/lnps.csv", "a", encoding="utf-8")
hc = HTTPConnection("openapi.seoul.go.kr", 8088)
for start in range(1, 893002, 1000):
    hc.request("GET", "/575a4655496b636839386f58586542/xml/ListNecessariesPricesService/%d/%d" % (start, start + 999)) 
    resBody = hc.getresponse().read()
    
    lnpsData = fromstring(resBody)
    for l in lnpsData.iter("row"):
        if l.find("A_NAME").text:
            f.write(l.find("M_NAME").text.replace(",", " ") + ",")
            f.write(l.find("A_NAME").text.replace(",", " ") + ",")
            f.write(l.find("A_PRICE").text + ",")
            f.write(l.find("P_DATE").text + ",")
            f.write(l.find("M_TYPE_NAME").text + ",")
            f.write(l.find("M_GU_NAME").text + "\n")
    print(start)
hc.close()
f.close()