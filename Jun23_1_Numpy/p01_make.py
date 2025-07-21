# SQL/객체 list/Pandas 놔두고 NumPy?
# 1) Pandas/sklearn/TF...들이 쓰니
# 2) 인공신경망(사실은 행렬계산)
#       행렬이 list -> 쌩 list보다는 NumPy가 좋고

# -> 값은 AI가 찾아낼텐데, 형태는 지정해줘야
import numpy as np

a = np.zeros([3, 2], dtype=np.int64)
print(a)
print(a.dtype)

b = np.ones([3, 2])
print(b, b.dtype)

c = np.empty([3, 2]) # 값 신경쓰지 말고 3x2로
print(c, c.dtype)

d = np.arange(2, 10, 3) # Python의 range같은
print(d)

e = np.random.rand(3, 2) # 0.0 ~ 0.9999 랜덤 3x2
print(e)

f = np.random.randn(3, 2) # 평균이 0, 표준편차 1 랜덤 3x2 -> 이걸 많이들 쓰던
print(f)

g = np.random.randint(1, 10, [3, 2]) # 1 ~ (10 - 1) 랜덤 3x2
print(g)