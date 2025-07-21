import pandas as pd

df = pd.read_csv("C:/ljw/lnps2.csv", names=["마트", "품명", "가격", "날짜", "종류", "구"])
print(df)

# 결측치

print(df["품명"].isnull()) # 값이 없나 확인
print(df[df["품명"].isnull()])
print("-----")

# 없는 거 채우기
df["품명"] = df["품명"].fillna("몰라")
print(df[df["품명"].isnull()])
print("-----")

# 있는 값 없애기
# 없다가 pandas로 표현 불가 -> numpy로
import numpy as np
df["품명"] = df["품명"].replace("몰라", np.nan)
print(df[df["품명"].isnull()])
print("-----")

# 0이면 계산이 가능
# 아예 없으면 계산 자체가 불가능
# 없는 걸 뭔가로 채워놓든지, 계산에서 빼든지
