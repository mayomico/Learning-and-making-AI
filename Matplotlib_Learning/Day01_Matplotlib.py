import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-10,10,1000)
# y=x**2
# plt.plot(x, y)
# y=np.sin(x)
# plt.plot(x, y)
# y=x**3
# plt.plot(x, y)
y=np.exp(-x**2/2)
plt.plot(x,y)
plt.title("Quadratic Function")
plt.xlabel("X")
plt.ylabel("Y")

plt.grid(True)#是否有网格？

plt.xlim(-10, 10)
plt.ylim(0, 1)
plt.show()