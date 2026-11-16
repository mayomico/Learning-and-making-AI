import numpy as np
# 任务 1：创建一个包含 1 到 10 的数组
# 任务 2：计算数组所有元素的总和
# 任务 3：计算数组的平均值
# 任务 4：让所有元素乘以 3
# 任务 5：创建一个长度为 10 的全零数组
# 任务 6：创建一个长度为 10 的全一数组
# 任务 7：输出数组的维度和形状
#test1
a=np.arange(1,11)
print(a)
#test2
print("sum=",np.sum(a))
#test3
print("mean=",np.mean(a))
#test4
print("mult=",a*3)
#test5
b=np.zeros(10)
print(b)
#test6
c=np.ones(10)
print(c)
#test7
print(np.ndim(c))
print(np.shape(c))
