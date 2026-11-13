# AMATH 301 RAY ZHOU
import numpy as np
import scipy as scp

a = 0.1
x_true = lambda t: np.e**(-a * t /2) * (np.cos(t) - a * np.sin(t) / 2)
A1 = x_true(20)

f = lambda t, x: - a * x - (1+ a**2 / 4) * np.e**(-a * t / 2) * np.sin(t)
A2 = f(3,5)

x_0 = 1
def forward_approximation(start,end,dt):
    N = int(np.round((end-start)/dt))
    t = np.linspace(start,end,N+1)
    x = np.zeros(t.size)
    x[0] = x_0
    for i in range (N):
        x[i + 1] = x[i] + dt * f(t[i],x[i])

    return x.copy(), np.max(np.abs(x - x_true(t)))

A3,A4 = forward_approximation(0,20,0.1)
A5, A6 = forward_approximation(0,20,0.01)
A7 = A4 / A6

fx1 = lambda t,x_i, dt: (x_i +  - dt * (1 + a**2 / 4) * np.exp(-a * t / 2) * np.sin(t)) / (1 + a * dt)
def backwards_approximation(start,end,dt):
    N = int(np.round((end-start)/dt))
    t = np.linspace(start,end,N+1)
    x = np.zeros(t.size)
    x[0] = x_0
    for i in range (N):
        x[i + 1] = fx1(t[i+1],x[i], dt)

    return x.copy(), np.max(np.abs(x - x_true(t)))

A8, A9 = backwards_approximation(0,20,0.1)
A10, A11 = backwards_approximation(0,20,0.01)
A12 = A9 / A11

def RK4(start,end,dt):
    N = int(np.round((end-start)/dt))
    t = np.linspace(start,end,N+1)
    x = np.zeros(t.size)
    x[0] = x_0
    for i in range (N):
        f1 = f(t[i] , x[i])
        f2 = f(t[i] + dt/2,x[i] + dt * f1 /2)
        f3 = f(t[i] + dt/2,x[i] + dt * f2 /2)
        f4 = f(t[i] + dt,x[i] + dt * f3) 
        x[i + 1] = x[i] + dt * (f1 + 2 * f2 + 2 * f3 + f4) / 6

    return x.copy(), np.max(np.abs(x - x_true(t)))

A13,A14 = RK4(0,20,0.1)


#problem 2

R = 1e-5
C = 1
x_0 = 0
v_source = lambda t: np.where(t < 4e-4, 0, 5)

t = np.linspace(0, 1e-3, 101)
A15 = v_source(t)

f = lambda t,v: (v_source(t) - v) / (R * C)
A16 = f(9,4)

A17,arr = forward_approximation(0,1e-3,1e-7)
A18,arr = forward_approximation(0,1e-3,2e-5)

def A19_backwards_approximation(start,end,dt):
    N = int(np.round((end-start)/dt))
    t = np.linspace(start,end,N+1)
    x = np.zeros(t.size)
    x[0] = x_0
    tol = 1e-8
    for i in range (N):
        a = -1
        b = 6   
        g = lambda z: z - x[i] - dt * f(t[i + 1], z)
        for j in range (1000):
            z = (a + b) / 2
            if np.abs(g(z)) < tol:
                break
            if g(z) < 0: a = z
            else: b = z
        z = (a + b) / 2
        x[i + 1] = z

    return x.copy()

A19 = A19_backwards_approximation(0,1e-3,2e-5)

A20 = np.mean(np.diff(
    scp.integrate.solve_ivp(f,(0,1e-3),[0],method='RK45').t
    ))
A21 = np.mean(np.diff(
    scp.integrate.solve_ivp(f,(0,1e-3),[0],method='Radau').t
    ))

#problem 3
f = lambda t,x: 8 * np.sin(x)
x_0 = np.pi / 4

dt = 0.2
A22 = forward_approximation(0,2,dt)

def A23_backwards_approximation(start,end,dt):
    N = int(np.round((end-start)/dt))
    t = np.linspace(start,end,N+1)
    x = np.zeros(t.size)
    x[0] = x_0
    tol = 1e-10
    for i in range (N):
        a = 0
        b = 4   
        g = lambda z: z - x[i] - dt * f(t[i + 1], z)
        dg = lambda z: 1 - dt * 8 * np.cos(z)
        z = x[i]
        for j in range (1000):
            if np.abs(g(z)) < tol:
                break
            z = z - g(z) / dg(z)
        x[i + 1] = z
        
    return x.copy()

A23 = A23_backwards_approximation(0,2,0.2)

A24 = scp.integrate.solve_ivp(f, (0, 2), [np.pi / 4], method="RK45").y[0].copy()
