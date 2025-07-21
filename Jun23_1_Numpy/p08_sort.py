import numpy as np

a = np.random.randint(1, 101, [10])
print(a)
print(a[1])
print(a[2:5]) # 2 ~ (5 - 1)
print(a[2:8:3]) # 2 ~ (8 - 1), 3칸씩
print(a[:8:3]) # 0 ~ (8 - 1), 3칸씩
print(a[2::3]) # 2 ~ 끝까지, 3칸씩
print(a[2:8:]) # 2 ~ (8 - 1), 1칸씩
print(a[::2]) # 0 ~ 끝까지, 2칸씩
print(a[::-1]) # 0 ~ 끝까지, -1칸씩 -> 역순
print("-----")

b = np.sort(a) # 오름차순
print(b)
print("-----")

c = np.sort(a)[::-1] # 내림차순 x -> 오름차순 + 역순
print(c)
print("-----")

d = np.random.randint(1, 101, [3, 5])
print(d)
print("-----")

e = np.sort(d) # 행별 오름차순 정렬(axis=1이 기본)
print(e)
print("-----")

f = np.sort(d, axis=0) # 열별 오름차순
print(f)
print("-----")

g = np.sort(d, axis=0)[::-1] # 열별 내림차순
print(g)
print("-----")

# h = np.sort(d)[::-1] # 행별 내림차순? x
h = np.sort(d)
for i in range(len(h)):
    h[i] = h[i][::-1] # 행별 내림차순
print(h)

i = []
for row in d:
    i.append(np.sort(row)[::-1])
i = np.array(i)
print(i)
print("-----")


