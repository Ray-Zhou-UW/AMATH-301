# # AMATH 301 RAY ZHOU
# import numpy as np
# import pandas as pd

# df = pd.read_csv("hw3_array.csv")
# x = df["x"].to_numpy()

# A1 = x.size

# A2 = x[-1]

# A3 = x[x>0].size

# A4 = x[x<0].size

# fib = np.zeros(31)
# A5 = fib.copy()

# fib[1] = 1

# for i in range(2,len(fib)):
#     fib[i] = int(fib[i-1] + fib[i-2])

# A6 = fib.copy()

# print (fib[20])

# A7 = fib[30] / fib [29]

# fib_even = fib[fib % 2 == 0].copy()
# fib_odd = fib[fib % 2 != 0].copy()
# A8 = fib_even.copy()
# A9 = fib_odd.copy()

# def harmonic(k,n):
#     if k > n:
#         return
#     s = 0
#     for i in range(k,n+1):
#         s = s + k / i
#     return s

# A10 = harmonic(1,2)
# A11 = harmonic(1,10)

# def smallestnumber(n):
#     i = 0
#     total = 0
#     while total <= n:
#         i += 1
#         total += 1 / i
#     return i

# A12 = smallestnumber(5)
# A13 = smallestnumber(17)

# f_x = lambda x: x**3 - (6/5) * x**2 - 9/5 * x + 1/2 

# def rootfinder(a,b,max_steps,tol,output):
#     for k in range(max_steps):
#         x = (a + b) / 2
#         if np.abs(f_x(x)) < tol:
#             # print("We found a root")
#             break
#         if np.sign(f_x(x)) == np.sign(f_x(a)):
#             a = x
#         else:
#             b = x
#     if output == 0:
#         return (a + b) / 2
#     if output == 1:
#         return k + 1

# A14 = f_x(0) * f_x(1)
# A15 = rootfinder(0,1,1000,1e-8,0)

# # print("This took {} steps".format(k + 1))
# # print("There is a root in the interval [{}, {}]".format(a, b))
# # print("Our guess for the root is x = {}".format(x))

# A16 = f_x(-2) * f_x(3)
# A17 = rootfinder(-2,3,1000,1e-8,0)
# A18 = rootfinder(-2,3,1000,1e-8,1)

# def falseposrootfinder(a,b,max_steps,tol,output):
#     for k in range(max_steps):
#         x = b - f_x(b) * ((b - a) / (f_x(b) - f_x(a)))
#         if np.abs(f_x(x)) < tol:
#             # print("We found a root")
#             break
#         if np.sign(f_x(x)) == np.sign(f_x(a)):
#             a = x
#         else:
#             b = x
#     if output == 0:
#         return x
#     if output == 1:
#         return k + 1

# A19 = falseposrootfinder(-2,3,1000,1e-8,0)
# A20 = falseposrootfinder(-2,3,1000,1e-8,1)