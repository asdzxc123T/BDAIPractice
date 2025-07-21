# db 미세먼지
# 종로구
from time import strftime
from oracledb import connect
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

con = connect("ljw100/91270290@195.168.9.68:1521/xe")
sql = "select * from seoul_dust where s_msrste_nm = '종로구' order by s_date"
df = pd.read_sql(sql, con)
con.close()

def changeDate(d):
    return d.strftime("%m/%d %H시")

df["S_DATE"] = df["S_DATE"].apply(changeDate)
print(df)
date = df["S_DATE"].to_numpy()
pm10 = df["S_PM10"].to_numpy()
pm25 = df["S_PM25"].to_numpy()

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name()
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False

_, sub1Conf = plt.subplots()
p1 = sub1Conf.plot(pm10, "r")
sub1Conf.set_xlabel("날짜")
sub1Conf.set_ylabel("미세먼지")

sub2Conf = sub1Conf.twinx()
p2 = sub2Conf.plot(pm25, "b")
sub2Conf.set_ylabel("초미세먼지")

sub1Conf.legend(p1 + p2, ["미세먼지", "초미세먼지"])
plt.title("종로구 미세먼지")
plt.xticks(np.arange(len(date)), date)
plt.show()
