# AMATH 301 RAY ZHOU
import numpy as np
import pandas as pd
import scipy as scp

df = pd.read_csv("horizons_data.csv")
delta = df["delta"].to_numpy()

A1 = delta.size
A2 = np.argmin(delta)

A3 = delta.size - 2

A4 = (delta[2:] - delta[:-2]) / 2

A5 = (delta[1] - delta[0]) / 1

A6 = (delta[-1] - delta[-2]) / 1

A7 = (-3 * delta[0] + 4 * delta[1] - delta[2]) / 2

A8 = (3 * delta[-1] - 4 * delta[-2] + delta[-3]) / 2

A9 = np.trapezoid(delta, dx=1) / (delta.size - 1)

x1 = np.array([1, 2, 3])
y1 = np.array([0, 2.5, 6])

A10 = (y1[1] - y1[0]) / (x1[1] - x1[0])
A11 = (y1[2] - y1[0]) / (x1[2] - x1[0])
A12 = (y1[2] - y1[1]) / (x1[2] - x1[1])

x2 = np.array([0.5, 3, 3.5])
y2 = np.array([5, 10, 2.5])

A13 = (y2[1] - y2[0]) / (x2[1] - x2[0])
A14 = (y2[2] - y2[0]) / (x2[2] - x2[0])
A15 = (y2[2] - y2[1]) / (x2[2] - x2[1])

x3 = np.array([0, 1, 4.5, 5, 6.5, 7, 10])
y3 = np.array([10, 3, 2, 0.5, 0.5, 1, 6.5])

A16 = (y3[4] - y3[2]) / (x3[4] - x3[2])

def approximate_derivative(x,y,k):
    if k == 0:
        dy_k = (y[k+1] - y[k]) / (x[k+1] - x[k])
    elif k == len(x) - 1:
        dy_k = (y[k] - y[k-1]) / (x[k] - x[k-1])
    else:
        dy_k = (y[k+1] - y[k-1]) / (x[k+1] - x[k-1])
    return dy_k


# Problem 3: kitten birth weights
mu = 85
sigma = 8.3

def kitten_density(x):
    return np.exp(-(x - mu)**2 / (2 * sigma**2)) / np.sqrt(2 * np.pi * sigma**2)

A17 = scp.integrate.quad(kitten_density, 110, 130)[0]

dx = 1
x_left = np.arange(110, 130, dx)  # Left endpoints: 110 through 129
left_approx = dx * np.sum(kitten_density(x_left))
A18 = abs(left_approx - A17)

A19 = np.zeros(10)
for j in range(1, 11):
    dx = 2.0**(-j)
    x_left = np.arange(110, 130, dx)
    left_approx = dx * np.sum(kitten_density(x_left))
    A19[j - 1] = abs(left_approx - A17)

A20 = np.zeros(10)
for j in range(1,11):
    dx = 2.0**(-j)
    x_right = np.arange(110 + dx, 130 + dx, dx)
    right_approx = dx * np.sum(kitten_density(x_right))
    A20[j - 1] = abs(right_approx - A17)

A21 = np.zeros(10)
for j in range(1,11):
    dx = 2.0**(-j)
    x_trap = np.arange(110, 130 + dx, dx)
    trap_approx = np.trapezoid(kitten_density(x_trap), dx=dx)
    A21[j - 1] = abs(trap_approx - A17)

A22 = np.zeros(10)
for j in range(1, 11):
    dx = 2.0**(-j)
    x_simpson = np.arange(110, 130 + dx, dx)
    y_simpson = kitten_density(x_simpson)
    simpson_approx = (dx / 3) * (
        y_simpson[0] + y_simpson[-1]
        + 4 * np.sum(y_simpson[1:-1:2])
        + 2 * np.sum(y_simpson[2:-1:2])
    )
    A22[j - 1] = abs(simpson_approx - A17)
