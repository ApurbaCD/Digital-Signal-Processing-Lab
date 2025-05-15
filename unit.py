import numpy as np
import matplotlib.pyplot as plt


t = np.arange(-1,1, 0.01)
n=np.linspace(0,10,10)

# print(t)
a=np.sin(n);
print(a)
# print(n)
plt.xlabel("time")
plt.ylabel("value")
plt.plot(n,a)
plt.show()