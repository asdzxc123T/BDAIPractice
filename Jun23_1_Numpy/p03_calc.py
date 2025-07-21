import numpy as np

a = np.random.randint(1, 11, [2, 3])
b = np.random.randint(1, 11, [2, 3])
print(a)
print(b)
print("-----")
c = a + b # 연산자를 써서 해도 되는데
print(c)
print("-----")
d = np.add(a, b)
print(d)
print("-----")
e = np.subtract(a, b)
print(e)
print("-----")
f = np.multiply(a, b)
print(f)
print("-----")
g = np.divide(a, b)
print(g)
print("-----")
h = np.mod(a, b)
print(h)
print("-----")
i = np.power(a, b)
print(i)
print("-----")

# greater, greater_equal, less, less_equal
j = np.less_equal(a, b)
print(j)
print("-----")

k = np.maximum(a, b) # 큰 것만 <=> minimum
print(k)
print("-----")

name = np.array(["홍길동", "김길동", "이길동"])
kor = np.array([100, 90, 60])
eng = np.array([10, 60, 80])
mat = np.array([50, 40, 100])
# 평균 60 넘는 학생 이름
avg = np.divide(np.add(np.add(kor, eng), mat), 3)
print(avg)
 
over60 = np.greater(avg, 60)
print(over60)
print(name[over60])
# print(name[kor == 100])
 
# print(name[(eng > 50) & (eng < 70)])