import numpy as np

# 任务1：创建一个 2×3 矩阵
A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# 任务2：求转置矩阵
A_T = A.T

print(A_T)
print(A_T.shape)


# 任务3：创建一个可逆矩阵
B = np.array([
    [3, 1],
    [2, 1]
], dtype=float)

# 求行列式
det_B = np.linalg.det(B)

# 求逆矩阵
B_inv = np.linalg.inv(B)

print(det_B)
print(B_inv)


# 任务4：验证 B @ B_inv 是否为单位矩阵
print(B @ B_inv)


# 任务5：创建一个不可逆矩阵
C = np.array([
    [1, 2],
    [2, 4]
], dtype=float)

# 判断 C 是否可逆
print(np.linalg.det(C))
print(np.linalg.matrix_rank(C))