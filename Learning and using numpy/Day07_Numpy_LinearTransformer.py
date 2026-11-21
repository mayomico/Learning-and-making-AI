
import numpy as np
import matplotlib.pyplot as plt

# 定义变换矩阵
# A = np.array([
#     [1.5, 0.5],
#     [0.3, 1.2]
# ])
#
# # 1. 恒等变换
# A = np.eye(2)
#
# # 2. 非均匀缩放
# A = np.array([
#      [2, 0],
#     [0, 0.5]
#  ])
#
# # 3. 旋转45度
theta = np.pi / 4

A = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])
#
# # 4. 剪切变换
# A = np.array([
#     [1, 1],
#     [0, 1]
# ])
#
# # 5. 降维映射
# A = np.array([
#     [1, 2],
#     [2, 4]
# ])

# 生成原始二维网格
t = np.linspace(-2, 2, 100)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 生成并绘制网格
for i in range(-2, 3):

    vertical = np.column_stack((
        np.full_like(t, i), t
    ))

    horizontal = np.column_stack((
        t, np.full_like(t, i)
    ))

    # 原始网格
    axes[0].plot(vertical[:, 0], vertical[:, 1])
    axes[0].plot(horizontal[:, 0], horizontal[:, 1])

    # 行向量形式存储点，因此使用 A.T
    vertical_new = vertical @ A.T
    horizontal_new = horizontal @ A.T

    # 变换后的网格
    axes[1].plot(
        vertical_new[:, 0],
        vertical_new[:, 1]
    )

    axes[1].plot(
        horizontal_new[:, 0],
        horizontal_new[:, 1]
    )

# 绘制变换后的两个基向量
for j in range(2):
    v = A[:, j]

    axes[1].quiver(
        0, 0, v[0], v[1],
        angles="xy",
        scale_units="xy",
        scale=1
    )

axes[0].set_title("Original Space")
axes[1].set_title("Transformed Space")

for ax in axes:
    ax.set_aspect("equal")
    ax.grid(True)
    ax.axhline(0)
    ax.axvline(0)

axes[0].set_xlim(-2.5, 2.5)
axes[0].set_ylim(-2.5, 2.5)

axes[1].set_xlim(-5, 5)
axes[1].set_ylim(-5, 5)

plt.tight_layout()
plt.show()

print("Determinant:", np.linalg.det(A))
print("Rank:", np.linalg.matrix_rank(A))
print("Inverse:\n", np.linalg.inv(A))
