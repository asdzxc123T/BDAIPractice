# NumPy
#   실제 사용은 np.array
#   기능 추가된 list
#   요즘 시대에 2차원/3차원 list?
#   -> 선수과정이니까...

# Pandas(Python Data Analysis Library)
#   실제 사용은 pd.DataFrame
#   코딩으로 하는 엑셀, R
#   엑셀 놔두고?
#   -> 대용량 데이터 때문에...
####################################################3
# pip install pandas
import pandas as pd

# list스러운 거
a = pd.Series([4231, 56, 2437, 1235])
print(a)
print(a[1])
print("-----")

# MS Excel스러운 거
b = pd.DataFrame()
b["이름"] = ["새우깡", "양파링"]
b["가격"] = [3000, 4000]
print(b)
print("-----")
print(b["이름"])
print("-----")
# Pandas가 원본 데이터에 영향 안 가는 걸 추구
# index : 찾는 기준
b = b.set_index(b["이름"])
print(b)
print("-----")
print(b.loc["새우깡"]) # index로 찾기
print("-----")
print(b.iloc[1]) # 0, 1, 2... 로 찾기
