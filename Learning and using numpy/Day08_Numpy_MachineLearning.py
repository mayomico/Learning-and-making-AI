import numpy as np
import matplotlib.pyplot as plt
X1=np.random.randint(0,10,(100,1))
X2=np.random.randint(0,10,(100,1))
noise=np.random.normal(0,1,(100,1))
Y=3*X1-2*X2+0.8+noise
LearningRate=0.001
A1=0.5
A2=0.5
#Predict Y=A1X1+A2X2+b
b=0
#training 1000 times
for i in range(10000):
    y=A1*X1+A2*X2+b
    error=Y-y#误差值为真实值减预测值
    A1=A1+LearningRate*(1/50*np.sum(error*X1))
    A2=A2+LearningRate*(1/50*np.sum(error*X2))
    b=b+LearningRate*(1/50*np.sum(error))
print("A1:",A1)
print("A2:",A2)
print("b:",b)
plt.subplot(1,2,1)
x=np.linspace(-10,10,100)
y=A1*x+b
plt.title("Training Picture(A2=0,X1~Y)")
plt.xlabel("X1")
plt.ylabel("Y")
plt.xlim(-10,10)
plt.ylim(-35,35)
plt.plot(x,y)
plt.scatter(X1,3*X1+0.8+noise)
plt.subplot(1,2,2)
x=np.linspace(-10,10,100)
y=A2*x+b
plt.title("Training Picture(A1=0,X2~Y)")
plt.xlabel("X2")
plt.ylabel("Y")
plt.xlim(-10,10)
plt.ylim(-25,25)
plt.plot(x,y)
plt.scatter(X2,-2*X2+0.8+noise)
plt.tight_layout()
plt.show()