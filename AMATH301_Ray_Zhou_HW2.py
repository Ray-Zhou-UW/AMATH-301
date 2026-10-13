# AMATH 301 RAY ZHOU
import numpy as np

x = np.linspace(0, 1, 5) * np.pi
A1 = np.copy(x)

u = np.cos(np.arange(0,399,0.5))
# u = np.arange(0,399,0.5)
A2 = np.copy(u)

A3 = u[421]

A4 = u[-3]

u1 = u
u1[28] = 4
A5 = np.copy(u1)

u2 = u[-400:]
A6 = np.copy(u2)

v = np.flip(u)
A7 = np.copy(v)

w = np.copy(u)
w[1::2] = v[1::2]
A8 = np.copy(w)

y = np.sin(u) / (v**2 + 1)
A9 = np.copy(y)


