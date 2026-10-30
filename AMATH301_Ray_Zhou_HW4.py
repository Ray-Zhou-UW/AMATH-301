# AMATH 301 RAY ZHOU
import numpy as np

# rng = np.random.default_rng(seed=301)
# x1 = rng.uniform(low=0.0, high=10.0, size=100)
# x2 = rng.uniform(low=0.0, high=10.0, size=10_000)

# A1 = x1.copy()
# A2 = x2.copy()

# A3 = x1.mean()
# A4 = np.sqrt(np.sum((x1 - x1.sum() / x1.size)**2) / (x1.size - 1))

# z = (x2 - A3) / A4
# A5 = z.copy()

# def calculate_statistics(arr):
#     mean = arr.mean()
#     std = arr.std()
#     return mean, std

# mu, sig = calculate_statistics(x1)

# def standardize_data(arr,mean,std):
#     zscore = (arr - mean) / std
#     return zscore

f = lambda x: np.e**(0.5*x) - 2
fdx = lambda x: 0.5 * np.e**(0.5*x)

x = 2.75
A6 = x - f(x) / fdx(x)
A7 = A6 - f(A6) / fdx(A6)

tol = 1e-8
for i in range(1000):
    x_new = x - f(x) / fdx(x)
    if np.abs(x_new - x) < tol:
        A8 = x_new 
        A9 = i
        break
    x = x_new

def newton(f_x,f_xdx,x,tol,max_steps):
    for i in range(max_steps):
        x_new = x - f_x(x) / f_xdx(x)
        if np.abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x_new
