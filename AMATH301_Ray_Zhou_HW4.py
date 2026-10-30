# AMATH 301 RAY ZHOU
import numpy as np
import scipy as scp

# rng = np.random.default_rng(seed=301)
# x1 = rng.uniform(low=0.0, high=10.0, size=100)
# x2 = rng.uniform(low=0.0, high=10.0, size=10_000)

# A1 = x1.copy()
# A2 = x2.copy()

# A3 = x1.mean()
# A4 = np.sqrt(np.sum((x1 - x1.sum() / x1.size)**2) / (x1.size - 1))

# z = (x2 - A3) / A4
# A5 = z.copy()

def calculate_statistics(arr):
    mean = arr.mean()
    std = np.sqrt(np.sum((arr - arr.sum() / arr.size)**2) / (arr.size - 1))
    return mean, std

# mu, sig = calculate_statistics(x1)

# def standardize_data(arr,mean,std):
#     zscore = (arr - mean) / std
#     return zscore

# f = lambda x: np.e**(0.5*x) - 2
# fdx = lambda x: 0.5 * np.e**(0.5*x)

# x = 2.75
# A6 = x - f(x) / fdx(x)
# A7 = A6 - f(A6) / fdx(A6)

# tol = 1e-8
# for i in range(1000):
#     x_new = x - f(x) / fdx(x)
#     if np.abs(x_new - x) < tol:
#         A8 = x_new 
#         A9 = i
#         break
#     x = x_new

# def newton(f_x,f_xdx,x,tol,max_steps):
#     for i in range(max_steps):
#         x_new = x - f_x(x) / f_xdx(x)
#         if np.abs(x_new - x) < tol:
#             return x_new
#         x = x_new
#     return x_new

def ellipse_perimeter(a, b):
    # The perimeter of an ellipse is P = 4aE(e^2), where e is the
    # eccentricity defined by e^2 = 1 - (b / a)^2.
    e = np.sqrt(1 - (b / a) ** 2)
    P = 4 * a * scp.special.ellipe(e ** 2)
    return P

# A10 = ellipse_perimeter(5,1)

P_b = lambda b: ellipse_perimeter(5,b)

A11 = P_b(4)

a = 1
b = 4
tol =  1e-9
for i in range(1000):
    x = (a + b) / 2
    if np.abs(P_b(x) - 25) < tol:
        # A12 = x
        A13 = i + 1
        break
    if np.sign(P_b(x) - 25) == np.sign(P_b(a) - 25):
        a = x
    else:
        b = x

# x = np.arange(1,4.05,0.1)
# P_x = P_b(x)
# db = 0.01
# A14 = P_x.copy()

# A15 = (P_b(x + db) - P_b(x)) / db
# A16 = (P_b(x) - P_b(x - db)) / db
# A17 = (P_b(x + db) - P_b(x - db)) / (2 * db)


