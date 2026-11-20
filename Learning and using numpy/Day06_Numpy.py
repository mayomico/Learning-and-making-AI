import numpy as np
# 实验1：实现可复用线性层
# 编写一个 Linear 函数：
# 要求：
# - 能够处理不同数量的样本。
# - 能够处理不同的输入特征数量。
# - 能够处理不同的输出特征数量。
def linear(w,x,b1):
    return w@x+b1
X = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])
# 实验2：观察权重变化
# 分别使用下面三个矩阵：
W1 = np.eye(2)

W2 = np.array([
    [2, 0],
    [0, 3]
])

W3 = np.array([
    [0, 1],
    [1, 0]
])
# 计算：
# Y_1=XW_1
# Y_2=XW_2
# Y_3=XW_3
# 观察三个结果，并解释它们的几何意义。
print(linear(X,W1,0))
print(linear(X,W2,0))
print(linear(X,W3,0))
# 实验3：检查维度
X = np.random.randn(32, 10)
W = np.random.randn(10, 5)
b = np.random.randn(5)
Y = X @ W + b
print(Y.shape)
# 然后改变 X 的样本数量为128。
#
# 观察：
# - W 是否需要改变？
# - b 是否需要改变？
# - 输出 shape 如何改变？