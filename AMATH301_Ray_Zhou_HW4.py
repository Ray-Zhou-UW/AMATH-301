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

def newton(f_x,f_xdx,x,tol,max_steps):
    x_new = x - f_x(x) / f_xdx(x)
    for i in range(max_steps):
        if np.abs(x_new - x) < tol:
            return x_new
        else:
            x_new = (x_new + x) / 2
            x_new = x - f_x(x) / f_xdx(x)
    return x_new


A6 = newton(f,fdx,2.75,1e-8,0)
A6 = newton(f,fdx,2.75,1e-8,1)