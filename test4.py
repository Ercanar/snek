#!/usr/bin/env python3

import numpy as np

a = np.arange(15).reshape(3, 5)
print(a)
b = np.arange(30).reshape(2, 3, 5)
print(b)
print(a.shape)
print(b.ndim)
c = np.array([[1,2],[3,4]])
print(c)

A = np.array([[1, 1],
              [0, 1]])

B = np.array([[2, 0],
              [3, 4]])

A * B     # elementwise product
A @ B     # matrix product
A.dot(B)  # another matrix product
