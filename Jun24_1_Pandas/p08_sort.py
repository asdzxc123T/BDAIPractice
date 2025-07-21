import pandas as pd

df = pd.read_csv("C:/ljw/titanic.csv")
df = df.set_index(df["Name"])
print(df)
print("-----")

# index 기준 정렬
df = df.sort_index(ascending=False)
print(df)
print("-----")

# 필드명 순 정렬
df = df.sort_index(axis=1)
print(df)
print("-----")

# 기타 다른 필드로 정렬
# df = df.sort_values(by="Age")
df = df.sort_values(by=["Pclass", "Age"], ascending=[False, True])
print(df)
print("-----")

# for문 돌려서 하나씩 찍자
# print(df.index)
for n in df.index:
    print(df.loc[n])
    print("-----")