# AMATH 301 RAY ZHOU
import numpy as np

rng = np.random.default_rng(seed=301)
x1 = rng.uniform(low=0.0, high=10.0, size=100)
x2 = rng.uniform(low=0.0, high=10.0, size=10_000)

A1 = x1.copy()
A2 = x2.copy()

A3 = x1.mean()
A4 = x1.std()

z = (x2 - A3) / A4
A5 = z.copy()

def calculate_statistics(arr):
    mean = arr.mean()
    std = arr.std()
    return mean, std

mu, sig = calculate_statistics(x1)

def standardize_data(arr,mean,std):
    zscore = (arr - mean) / std
    return zscore


