import numpy as np
import matplotlib.pyplot as plt

n = np.arange(0, 20)

# ω = π
omega = np.pi
x = np.cos(omega * n)  # = (-1)^n

plt.stem(n, x)
plt.title(r'Discrete-Time Cosine with $\omega = \pi$: $\cos(\pi n) = (-1)^n$')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
