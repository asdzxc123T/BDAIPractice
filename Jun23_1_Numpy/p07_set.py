import numpy as np

a = np.random.randint(1, 11, [2, 3])
b = np.random.randint(1, 11, [2, 3])
print(a)
print(b)
print("-----")

c = np.intersect1d(a, b) # 교집합 : a, b 둘 다 있는 거
print(c)
print("-----")

d = np.union1d(a, b) # 합집합
print(d)
print("-----")

e = np.setdiff1d(a, b) # 차집합 (a에서 b에 있는 거는 빼고)
print(e)
print("-----")

f = np.setxor1d(a, b) # 한쪽에만 있는 거
print(f)
print("-----")

g = np.unique(a) # 중복 제거
print(g)
print("-----")

