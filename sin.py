import sys
import numpy as np
import matplotlib.pyplot as plt
print("hello,world")
# print(sys.version)

# angle_radians=np.pi
# print(angle_radians)
# sine_wave=np.sin(angle_radians)
# print(sine_wave)

# zero_sine=np.sin(0)

# extreme_sine=np.sin(np.pi) #sine of 180 degree

# print("sine of 0 radians",zero_sine)
# print("sine of pi radians",extreme_sine)
# print(np.pi)

# angles=np.array([0,np.pi/2,np.pi,3*np.pi/2])
# sine_values=np.sin(angles)
# print(sine_values)

# x=np.linespace(0,2*np.pi,100)
# y=np.sin(x);
# print(y)



# t = np.arange(0, 1.00, 0.001)
t = np.linspace(0, 1, 1000) #time array from 0 to 1
a = 10 #amplitude
f = 5  #frequency

# y = a * np.sin(2 * np.pi * f * t)
# y1 = a * np.cos(2 * np.pi * f * t)

# plt.figure(figsize=(10, 8))
# plt.subplot(2, 1, 1)
# plt.plot(t, y)
# # plt.plot(t,y1)
# plt.grid(True)
# plt.xlabel('Time, msec')
# plt.ylabel('Amplitude')
# # plt.title('Continuous-Time Signal x_{a}(t)')
# plt.axis([0, 1, -20, 20])
# plt.show()

T = 0.01
n = np.arange(0, 1, 0.01)
xs = a * np.sin(2 * np.pi * f * n)
k = np.arange(len(n))

# plotting the diecrete-time signal

plt.subplot(2, 1, 2)
plt.stem(k, xs)
plt.grid(True)
plt.xlabel('Time index n')
plt.ylabel('Amplitude')
plt.title('Discrete-time signal x[n]')
plt.axis([0, len(n) - 1, -10.2, 10.2])

plt.tight_layout()
plt.show()



