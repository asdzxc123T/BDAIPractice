import pandas as pd

df = pd.read_csv("C:/ljw/titanic.csv")
print(df)
print("-----")
# pandas는 원본에 영향 안 가게 -> 삭제가 의미가 있나?

# 필드 삭제 : 그 필드 말고 나머지만 추출
df = df.drop("Survived", axis=1) # Survived 필드 삭제
df = df.drop(["Pclass", "Cabin"], axis=1) # Pclass, Cabin 필드 삭제
# PassengerId, Sex, Age, SibSp, Parch, Ticket, Embarked 필드 삭제 -> Name, Fare 빼고 나머지 다
df = df[["Name", "Fare"]]

print(df)
print(df.columns)
print("-----")

# 데이터 삭제 : 
df = df.drop(890) # 890번 지우기 x, index로 지우기
df = df.set_index(df["Name"])
df = df.drop("Behr, Mr. Karl Howell")
# Graham, Miss. Margaret Edith 빼고 다 삭제 or
# 요금이 30 미만인 거 다 삭제
df = df[df["Fare"] >= 30]
print(df)
print("-----")

# 모기
df = pd.read_csv("C:/ljw/mosquito3.csv", names=["언제", "물가", "집", "공원"])
# 물가, 공원 필드 없애고
df = df[["언제", "집"]]
# 미측정된 거 없애고
df = df[df["집"] != "미측정"]
# 전체조회
print(df)
print("-----")
# 집 모기지수 평균값 : 왜 원래 df의 자료형을 살렸을까?

print(df["집"].mean())
print("-----")
