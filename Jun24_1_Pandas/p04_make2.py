from oracledb import connect
import pandas as pd

# csv(첫줄이 제목)
a = pd.read_csv("C:/ljw/titanic.csv")
print(a)
print("-----")

# csv(제목 없이 데이터만 있는 거)
b = pd.read_csv("C:/ljw/seoulDust.csv", names=["년", "월", "일", "시", "권역", "구", "미세", "초미세", "상태"])
print(b)
print("-----")

# 정형데이터 -> 주로 csv(데이터 자체에 , 있는 거는)
# 비정형데이터 -> 주로 txt
# txt(확장자는 허상 -> txt든 뭐든)
c = pd.read_csv("C:/ljw/naverNews.txt", sep="\t", names=["제목", "내용"])
print(c)
print("-----")

con = connect("ljw100/91270290@195.168.9.68:1521/xe")
sql = "select * from seoul_dust"
d = pd.read_sql(sql, con)
print(d)
con.close()