import pandas as pd

df = pd.read_csv("C:/ljw/titanic.csv")
print(df.columns)

# 등급별 산/죽은 사람 수
print(df.groupby(["Pclass", "Survived"])["Survived"].count())

# 등급별 평균요금
print(df.groupby("Pclass")["Fare"].mean())

# 성별별 산/죽은 사람 수
print(df.groupby(["Sex", 'Survived'])["Survived"].count())

# 객실 뭐뭐 있나(중복 제거)
print(df["Cabin"].unique())
print("-----")

# 객실 몇개
print(df["Cabin"].nunique())
print("-----")

# 객실별 몇명씩
print(df["Cabin"].value_counts())
print("-----")

# 물가
df = pd.read_csv("C:/ljw/lnps2.csv", names=["마트", "품명", "가격", "날짜", "종류", "구"])
# 마트(시장)가 뭐뭐있나
print(df["마트"].unique())
# 마트(시장)가 몇종류
print(df["마트"].nunique())
# 구별로 데이터 몇개씩
print(df["구"].value_counts())