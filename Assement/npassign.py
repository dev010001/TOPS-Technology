import numpy as np

# 1
arr_3d = np.arange(1, 25).reshape(2, 3, 4)
print("1\n", arr_3d, "\n")

# 2
rm = np.random.randint(10, 51, (5, 5))
even1 = rm[rm % 2 == 0]
print("2\n", rm)
print(even1, "\n")

# 3
a = np.arange(1, 13).reshape(3, 4)
b = np.array([10, 20, 30, 40])
sum1 = a + b
print("3\n", sum1, "\n")

# 4
identy = np.eye(6)
identy[np.arange(6), np.arange(5, -1, -1)] = 7
print("4\n", identy, "\n")

# 5
lin = np.linspace(-5, 5, 20).reshape(4, 5)
positive_vals = lin[lin > 0]
print("5\n", lin)
print(positive_vals, "\n")

# 6
mat = np.arange(1, 17).reshape(4, 4)
mat[[0, -1]] = mat[[-1, 0]]
print("6\n", mat, "\n")

# 7
rfloats = np.random.rand(10, 10)
max_sum_row = rfloats[np.argmax(rfloats.sum(axis=1))]
print("7\n", rfloats)
print(max_sum_row, "\n")

# 8
arr = np.arange(1, 26).reshape(5, 5)
submat = arr * (arr % 2 == 0)
print("8\n", submat, "\n")

# 9
a = np.array([1, 2, 3])
b = np.array([[10], [20], [30]])
result = a * b
print("9\n", result, "\n")

# 10
daig = np.full((4, 4), -1)
np.fill_diagonal(daig, [5, 10, 15, 20])
print("10\n", daig, "\n")

# 11
eye = np.eye(5) * np.arange(3, 18, 3)
print("11\n", eye, "\n")

# 12
arr = np.arange(1, 25).reshape(3, 4, 2)
flattened = arr.ravel()
reshaped = flattened.reshape(2, 3, 4)
print("12\n", reshaped, "\n")

# 13
rm = np.random.randint(1, 101, (7, 7))
rm[rm % 5 == 0] = -5
print("13\n", rm, "\n")

# 14
angles = np.linspace(0, 2*np.pi, 10)
sico = np.column_stack((np.sin(angles), np.cos(angles)))
print("14\n", sico, "\n")

# 15
checker = np.zeros((5, 5), dtype=int)
checker[::2, 1::2] = 1
checker[1::2, ::2] = 1
print("15\n", checker, "\n")
