# 물가
from oracledb import connect
import pandas as pd

df = pd.read_csv("C:/ljw/lnps2.csv", names=["마트", "품명", "가격", "날짜", "종류", "구"])
df = df.sort_values(by="가격", ascending=False)
print(df)
print("-----")
# 가격 말도 안 되는 거 없애고
df = df[df["가격"] < 1681580]
df = df[df["가격"] > 0]
print(df)
print("-----")
# 평균가
print(df["가격"].mean())
print("-----")

# 종류별 평균가
print(df.groupby("종류")["가격"].mean())
print("-----")

# 구 -> 종류별 평균가
print(df.groupby(["구", "종류"])["가격"].mean())

# db에 있는 미세먼지
con = connect("ljw100/91270290@195.168.9.68:1521/xe")
sql = "select * from seoul_dust"
df = pd.read_sql(sql, con)
con.close()
df["S_PM_SUM"] = df["S_PM10"] + df["S_PM25"]
# 구별 PM10+PM25 평균
print(df.groupby("S_MSRSTE_NM")["S_PM_SUM"].mean())
# 권역별 PM10+PM25 평균
print(df.groupby("S_MSRRGN_NM")["S_PM_SUM"].mean())
# 권역별 -> 구별 PM10+PM25 평균
print(df.groupby(["S_MSRRGN_NM", "S_MSRSTE_NM"])["S_PM_SUM"].mean())