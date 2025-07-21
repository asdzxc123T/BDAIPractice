import pandas as pd

df1 = pd.read_csv("C:/ljw/titanic.csv")
df2 = pd.read_csv("C:/ljw/titanic.csv")

df3 = pd.concat([df1, df2]) # df1 뒤에 df2
print(df3)

df4 = pd.concat([df1, df2], axis=1) # df1 옆에 df2
print(df4)
print("-----")

# join
snack = pd.DataFrame()
snack["이름"] = ["새우깡", "빼빼로"]
snack["가격"] = [3000, 2000]
snack["제조사"] = ["농심", "롯데"]

company = pd.DataFrame()
company["회사명"] = ["농심", "롯데"]
company["위치"] = ["서울", "수원"]

# 양쪽 다 제조사 필드 존재
# sc = pd.merge(snack, company)
# print(sc)

# 양쪽 다 존재하는 필드가 여러개면
# sc = pd.merge(snack, company, on="제조사")

# 양쪽 필드명이 다르면
sc = pd.merge(snack, company, left_on="제조사", right_on="회사명")
print(sc)
