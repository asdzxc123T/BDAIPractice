from oracledb import connect
import pandas as pd

df = pd.read_csv("C:/ljw/lnps.csv", names=["마트이름", "제품명", "가격", "날짜", "종류", "구"])

print(df["가격"].max())
# 저거 품명
print(df[df["가격"] == df["가격"].max()])
print(df["가격"].min())
print(df[df["가격"] == df["가격"].min()])
print(df["가격"].mean())
print("-----")
print(df["가격"].mode()) # 최빈값(자주 나오는) -> 결과가 Series로 나옴
print(df["가격"].sum())
print(df["가격"].count())
print(df["가격"].var())
print(df["가격"].std())
print(df["가격"].describe()) # 다
print("-----")

# 갖고 있는 미세먼지 데이터
# 미세 + 초미세 구해서
# 평균
# 최소값
# 가장 깨끗한 구 이름

con = connect("ljw100/91270290@195.168.9.68:1521/xe")
sql = "select * from seoul_dust"
dustDF = pd.read_sql(sql, con)
con.close()
dustDF["S_PM_SUM"] = dustDF["S_PM10"] + dustDF["S_PM25"]
print(dustDF)
print(dustDF["S_PM_SUM"].mean())
print(dustDF["S_PM_SUM"].min())
print(dustDF[dustDF["S_PM_SUM"] == dustDF["S_PM_SUM"].min()][["S_MSRSTE_NM"]])