import pandas as pd
import numpy as np

df = pd.read_csv("C:/ljw/mosquito3.csv", names=["언제", "물가", "집", "공원"])


# print(df[df["물가"].isnull()]) # 값이 없지는 않음
# print(df[df["물가"] == "미측정"]) # 미측정이라는 값이 들어가 있음
# print(df["물가"].dtype) # 604.9, 300.1, 미측정 -> pandas 입장에서는 object로 받을 수밖에
# print(df["물가"].mean()) # 자료형이 숫자가 아니니 -> 계산 불가

# 미측정 -> 없애자
df["물가"] = df["물가"].replace("미측정", np.nan)
df["집"] = df["집"].replace("미측정", np.nan)
df["공원"] = df["공원"].replace("미측정", np.nan)

# 필드 형변환
# ??? -> 숫자
df["물가"] = pd.to_numeric(df["물가"])
df["집"] = pd.to_numeric(df["집"])
df["공원"] = pd.to_numeric(df["공원"])

# 숫자 -> 문자
# df["물가"] = df["물가"].astype(str)

# 미측정된 거에는 필드별 평균값으로 채워서
df["물가"] = df["물가"].fillna(df["물가"].mean())
df["집"] = df["집"].fillna(df["집"].mean())
df["공원"] = df["공원"].fillna(df["공원"].mean())

# 물가, 집, 공원 평균치
# 언제 모기가 제일 심했나
df["평균"] = (df["물가"] + df["집"] + df["공원"]) / 3
print(df[df["평균"] == df["평균"].max()])
