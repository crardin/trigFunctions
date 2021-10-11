"""
Program to graph cos, sin, and tan from 0 to 2pi
"""
import matplotlib.pyplot as plt
import math
import numpy as np

if __name__ == "__main__":
    pass

theta = np.arange(0, 2*np.pi, 0.1)
sin_theta = np.sin(theta)
cos_theta = np.cos(theta)
tan_theta = np.tan(theta)

plt.figure(1)
plt.plot(theta, sin_theta)
plt.grid(True)
plt.show()

plt.figure(2)
plt.plot(theta, cos_theta)
plt.grid(True)
plt.show()

plt.figure(3)
plt.plot(theta, tan_theta)
plt.grid(True)
plt.show()




