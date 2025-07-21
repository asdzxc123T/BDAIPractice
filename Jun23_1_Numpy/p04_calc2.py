import numpy as np

a = np.random.randn(2, 3)
print(a)
print("-----")

b = np.ceil(a) # 올림
print(b)
print("-----")

c = np.floor(a) # 내림
print(c)
print("-----")

d = np.rint(a) # 반올림
print(d)
print("-----")

e = np.round(a, 2) # 자리수 지정 반올림
print(e)
print("-----")

# 소수점 이하 셋째자리에서 올림
f = np.divide(np.ceil(np.multiply(a, 100)), 100)
print(a)
print(f)
print("-----")

# 후속 기술들이 표현 못 하는
g = np.array([1, np.nan, 123, np.inf, 33])
print(g)
print("-----")
h = np.isnan(g)
print(h)
print("-----")
i = np.isinf(g)
print(i)
print("-----")

j = np.random.randint(-5, 6, [2, 3])
print(j)
print("-----")
k = np.abs(j)
print(k)
print("-----")
l = np.sqrt(j)
print(l)
print("-----")