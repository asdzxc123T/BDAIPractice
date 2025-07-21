import numpy as np

a = np.random.randint(1, 11, [10])
print(a)
print("-----")
a[1] = 999
a[2:5] = 888
print(a)
print("-----")
a = np.where(a % 2 == 0, 777, a) # 조건, 값, 대상
print(a)