import numpy as np

a = np.random.randint(1, 101, [3, 5])
b = np.random.randint(1, 101, [3, 5])
print(a)
print(b)
print("------")

c = a + b # 쌩list는 붙이는데, np.array는 계산
print(c)
print("------")

d = np.concatenate([a, b]) # 붙이기
print(d)
print("------")

e = np.append(a, b) # 붙여서 1차원으로
print(e)
print("------")
# axis=0 : 열
# axis=1 : 행
f = np.concatenate([a, b], axis=1) # 0이 기본
print(f)
print("------")
g = np.array_split(a, 2) # 멋대로 2개로
print(g)
print("------")
# h = np.split(a, 2) # 정확하게 2등분(갯수가 맞아떨어져야 가능)
h = np.split(a, 3) # 정확하게 3등분
print(h)
print("------")
