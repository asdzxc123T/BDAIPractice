import pandas as pd
# 물가.csv 불러서 df로
# 마트이름, 제품명, 가격, 날짜, 종류, 구
a = pd.read_csv("C:/ljw/lnps.csv", names=["마트이름", "제품명", "가격", "날짜", "종류", "구"])

# 마트이름으로 찾게 세팅
a = a.set_index(a["마트이름"])
# 마트이름 가나다순 정렬
a = a.sort_index()
# 한번 출력
print(a)
print("-----")

# 통인시장 데이터만
print(a.loc["통인시장"])
print("-----")

# 마트명에 '농협' 들어있는 데이터만
print(a[a["마트이름"].str.contains("농협")])
print("-----")

# 사과는 어떤 마트에 가면 살 수 있나(마트 이름)
print(a[a["제품명"].str.contains("사과")][["마트이름"]])

# 품명 가나다순 -> 가격 비싼순 정렬
a = a.sort_values(by=["제품명", "가격"], ascending=[True, False])
print(a)
print("-----")

# 30000원 이상인 데이터 품명, 가격
print(a[a["가격"] >= 30000][["제품명", "가격"]])
print("-----")

# 종로구 데이터만 반복문 돌려서 하나하나 출력
jongroDF = a[a["구"] == "종로구"]
for i, j in enumerate(jongroDF.index):
    print(jongroDF.iloc[i])