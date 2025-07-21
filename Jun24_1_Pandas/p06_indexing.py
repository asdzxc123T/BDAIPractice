import pandas as pd

a = pd.read_csv("C:/ljw/titanic.csv")
print(a)
print("-----")

# DF 기본 정보
print(a.shape)
print("-----")
print(a.columns) # 필드명
print("-----")
print(a.head())
print("-----")
print(a.tail(7))
print("-----")

# 열 기준 조회(특정 필드만 -> select)
print(a["Name"])
print("-----")
print(a.Name)
print("-----")
print(a[["Name", "Age"]])
print("-----")

# 행 기준 조회(특정 데이터 -> where)
print(a.iloc[1]) # 1번 데이터
print("-----")
print(a.iloc[1:5]) # 1 ~ (5 - 1)번 데이터
print("-----")
# index : 찾는 기준(primary key) - 기본적으로는 0, 1, 2, 3
a = a.set_index(a["Name"]) # index 바꾸기
print(a)
print("-----")
print(a.loc["Braund, Mr. Owen Harris"]) # index로 찾기
print("-----")
print(a.loc["Braund, Mr. Owen Harris":"Allen, Mr. William Henry"])
print("-----")

# 행 + 열 기준 조회(select ... where)
print(a.loc["Graham, Miss. Margaret Edith"]["Age"])
print("-----")
print(a.loc["Graham, Miss. Margaret Edith"][["Age", "Pclass"]])
print("-----")
print(a.loc["Graham, Miss. Margaret Edith", "Age"])
print("-----")
print(a.loc["Graham, Miss. Margaret Edith", ["Age", "Pclass"]])
print("-----")

# 조건 조회(where)
# print(a["Age"] > 30) # 나이가 30 초과 : True/False
print(a[a["Age"] > 30]) # 나이가 30 넘는
print("-----")
# 20대 : 20 <= 나이 < 30
# print(a[(a["Age"] >= 20) and (a["Age"] < 30)])
print(a[(a["Age"] >= 20) & (a["Age"] < 30)])
