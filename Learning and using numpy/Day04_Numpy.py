import numpy as np
# 任务一：三维张量
# - 使用 np.arange(48) 创建数组。
# - 将其转换成 (2,3,8)。
# - 输出 shape、ndim、size。
A=np.arange(48)
A=np.reshape(A,(2,3,8))
print(A.shape)
print(A.ndim)
print(A.size)
# 任务二：形状变换
# - 将任务一的数组转置成 (2,8,3)。
# - 将原数组 reshape 成 (6,8)。
# - 比较两种变换后的内容。
A=np.transpose(A,(0,2,1))
print(A)
A=np.reshape(A,(6,8))
print(A)
#任务三：向量与矩阵
#创建A = np.array([1, 2, 3, 4])
# - 一行四列的矩阵。
# - 四行一列的矩阵。
# 输出三个数组的 shape。
A=np.array([1,2,3,4])
print(A)
print(np.reshape(A,(1,4)))
print(np.reshape(A,(4,1)))
print(A.shape)
print(np.reshape(A,(4,1)).shape)
print(np.reshape(A,(1,4)).shape)
# 任务四：图像布局
# - 创建 (32,3,64,64) 的随机数组。
# - 转换为 (32,64,64,3)。
# - 验证转换前后 size 是否相同。
A=np.random.randint(1,100,(32,3,64,64))
print(A.size)
print(np.transpose(A,(0,3,1,2)).size)