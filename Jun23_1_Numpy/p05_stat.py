import numpy as np

a = np.random.randint(1, 11, [2, 3])
print(a)
print("-----")

b = np.sum(a)
print(b)
print("-----")

c = np.mean(a)
print(c)
print("-----")

d = a - c # 각 값에서 평균을 뺌(값이랑 평균이랑 얼마나 차이)
d = d ** 2 # 음수도 있어서 다 더해버리면 0? -> 제곱해서 음수를 없애자
d = np.mean(d) # 의 평균
print(d)
print("-----")

e = np.var(a) # 분산
print(e)
print("-----")

f = np.sqrt(d) # 분산 구한 거 루트(제곱을 했으니 단위가 달라진(길이 -> 넓이))
print(f)
print("-----")

g = np.std(a) # 표준편차
print(g)
print("-----")

h = np.max(a)
print(h)
print("-----")

i = np.min(a)
print(i)
print("-----")

j = np.max(a, axis=1)
print(j)
print("-----")

k = np.min(a, axis=0)
print(k)
print("-----")

print(a)
l = np.argmax(a) # 제일 큰 값이 있는 index(동률이면 앞에 걸로)
print(l)
m = np.argmin(a)
print(m)
n = np.argmax(a, axis=0)
print(n)
o = np.argmin(a, axis=1)
print(o)
print("-----")