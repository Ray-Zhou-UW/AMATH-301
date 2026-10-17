# AMATH 301 RAY ZHOU
import numpy as np

# x = np.linspace(0, np.pi, 5)
# A1 = x.copy()

# u = np.cos(np.arange(0,399.5,0.5))
# # u = np.arange(0,399.5,0.5)
# A2 = u.copy()

# A3 = u[421]

# A4 = u[-3]

# A5 = u.copy()
# A5[28] = 4

# A6 = u[-400:].copy()

# v = np.flip(u)
# A7 = v.copy()

# w = u.copy()
# w[1::2] = v[1::2]
# A8 = w.copy()

# y = np.sin(u) / (v**2 + 1)
# A9 = y.copy()

# temps = np.array([[52, 61, 47],
#                   [54, 63, 49],
#                   [49, 58, 44],
#                   [51, 60, 46]])
# A10 = temps.copy()

# A11 = temps[2, 1]

# A12 = temps[0, 2]

# A13 = temps[:, :2].copy()

# A14 = temps[2,:].copy()


a = np.linspace(0, 1, 19)
A15 = a.copy()

a_bool = (a > 0.3)
A16 = a_bool.copy()

a_big = a[a_bool]
A17 = a_big.copy()

x = np.linspace(-6,6,31)
A18 = x[np.sin(x) < 0.5].copy()

h = np.linspace(0, 10, 400)
T = 15 - 6.5 * h
A19 = h[T > 0].copy()

P = 101325 * (1 - 0.0225577 * h)**5.25588
A20 = P[T < 0].copy()

