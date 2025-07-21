import pandas as pd

df = pd.read_csv("C:/ljw/titanic.csv")
df = df[["Name", "Sex"]]
# male -> 남자, female -> 여자
df["Sex"] = df["Sex"].replace(["male", "female"], ["남자", "여자"])

# 순수 Python
# 글자를 넣어주면 그 글자에 있는 Mr. 부분을 미스터로 바꿔주는 함수
def changeMr(s):
    return s.replace("Mr.", "미스터")

# 이름 필드에서 Mr. -> 미스터
# df["Name"] = df["Name"].replace("Mr. ", "미스터")
df["Name"] = df["Name"].apply(changeMr)

# 이름 필드에서 성 빼고 이름만
# def getOnlyName(s):
#     return s.split(",")[0]
# df["Name"] = df["Name"].apply(getOnlyName)
df["Name"] = df["Name"].apply(lambda name: name.split(",")[0])

print(df)
print("-----")
df = pd.read_csv("C:/ljw/titanic.csv")
df = df[["Name", "Age", "Survived"]]

# 나이 -> 10대/20대/30대/...
df["Age"] = df["Age"].apply(lambda age: str(int(age // 10)) + "0대" if age >= 0 else "미상")
print(df)