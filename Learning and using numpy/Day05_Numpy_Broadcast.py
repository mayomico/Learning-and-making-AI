#广播 broadcast
import numpy as np
# 任务一：基础广播
# 分别计算：
# - A + B
# - A + C
# 打印结果与 shape。
A = np.arange(12).reshape(3, 4)#(3,4)
B = np.array([10, 20, 30, 40])#(1,4)
C = np.array([[100], [200], [300]])#(3,1)
print(A+B,(A+B).shape)
print(A+C,(A+C).shape)
# 任务二：模拟线性层
# 创建：
# - X.shape = (5,3)
# - W.shape = (3,2)
# - b.shape = (2,)
# 计算：
# Y=XW+b
# 检查最终输出是否为 (5,2)。
# 随后尝试把 b 改成 (5,1)，再次计算。解释为什么代码仍然可以运行，但它的数学意义发生了变化。
X=np.zeros((5,3))
W=np.zeros((3,2))
b=np.zeros((2,))
Y=X@W+b
print(Y.shape)