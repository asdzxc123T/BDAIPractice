# 서울 미세먼지

# 구별 미세 + 초미세 평균 구해서

# 제일 더러운 구 이름
# 제일 깨끗한 구
# 평균보다 못한 구
from datetime import datetime
from ljw.ljwDBManager import ljwDBManager
import numpy as np

# con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.68:1521/xe")
# sql = "select * from seoul_dust"
# cur.execute(sql)
# f = open("C:/ljw/seoulDust.csv", "w", encoding="utf-8")

# for s_date, s_msrrgn_nm, s_msrste_nm, s_pm10, s_pm25, s_idex_nm in cur:
#     t_date = datetime.strftime(s_date, "%Y,%m,%d,%H")
#     f.write(t_date +
#             "," + s_msrrgn_nm +
#             "," + s_msrste_nm +
#             "," + str(s_pm10) +
#             "," + str(s_pm25) +
#             "," + s_idex_nm + "\n"
#     )

# f.close()
# cur.close()
# con.close()

pmSum = {}
pmCount = {}
f = open("C:/ljw/seoulDust.csv", "r", encoding="utf-8")
for line in f.readlines():
    line = line.replace("\n", "").split(",")
    sum = int(line[6]) + int(line[7])
    if line[5] in pmSum:
        pmSum[line[5]] += sum
        pmCount[line[5]] += 1
    else:
        pmSum[line[5]] = sum
        pmCount[line[5]] = 1
f.close()

gu, pmAvg = [], []
for k, v in pmSum.items():
    gu.append(k)
    pmAvg.append(v / pmCount[k])
gu = np.array(gu)
pmAvg = np.array(pmAvg)
print(gu)
print(pmAvg)

# 가장 미세먼지가 심한 구 이름
print(gu[np.argmax(pmAvg)], np.max(pmAvg))

# 가장 미세먼지가 깨끗한 구 이름(동률 다 뜨게)
print(gu[pmAvg == np.min(pmAvg)], np.min(pmAvg))

# 평균보다 깨끗한 구 이름
print(gu[pmAvg < np.mean(pmAvg)])

# pm = []
# try:
#     con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.68:1521/xe")
#     sql = "SELECT s_msrste_nm, avg(s_pm10 + s_pm25) FROM seoul_dust GROUP BY s_msrste_nm order by avg(s_pm10 + s_pm25) desc"
#     cur.execute(sql)
#     for s_nm, a in cur:
#         pm.append([s_nm, a])
# except Exception as e:
#     print(e)
# finally:
#     ljwDBManager.closeConCur(con, cur)

# print(pm[0])
# print(pm[-1])

