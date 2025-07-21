import pandas as pd
a = pd.DataFrame()
a["이름"] = ["새우깡", "양파링"]
a["가격"] = [5000, 4000]
print(a)
print("-----")

# Pandas 1.x : append 써서 Series/dict도 추가하고 다 했었
# Pandas 2.x : 혼란스럽다고 append 삭제, DF끼리 붙이기만 살려놨음

# list(np.array) -> pd.Series(Series는 0, 1, 2, 3, ... 체제, DF은 필드명이 필요)
s = pd.Series(["빼빼로", 2000], index=["이름", "가격"])
# a = a.append(s) 2.x에서 삭제됨
s = pd.DataFrame([s]) # pd.Series -> pd.DF
a = pd.concat([a, s])
print(a)
print("-----")

# dict
s = {"이름": "포카칩", "가격": 6000}
s = pd.DataFrame([s]) # dict -> pd.DF
a = pd.concat([a, s])
print(a)
print("-----")


print("-----")