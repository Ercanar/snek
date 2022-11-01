#!/usr/bin/env python3

import math
import numpy as np
import matplotlib.pyplot as plt

L = 1
s = 500
# c = 20
# deltax = L / s
# deltat = deltax / c
y = np.zeros((s, s))

for t in range(s):
    for x in range(s):
        # always zero at boundaries
        if x == 0 or x == s - 1:
            y[x, t] = 0
        # base case: sine wave
        elif t == 0:
            y[x, t] = 5 * math.sin(4 * math.pi * x / s)
        # second base case: weird hack
        elif t == 1:
            y[x, t] = y[x, 0] + 0.5 * (
                y[x + 1, 0] +
                y[x - 1, 0] -
                2 * y[x, 0]
            )
        # all other timesteps
        else:
            y[x, t] = (
                2 * y[x, t - 1] -
                y[x, t - 2] + (
                    y[x + 1, t - 1] +
                    y[x - 1, t - 1] -
                    2 * y[x, t - 1]
                ))

# graph that shit
ax = plt.axes(projection="3d")
t = np.arange(len(y))
x = np.arange(len(y[0]))
(x, t) = np.meshgrid(x, t)
ax.plot_surface(x, t, y)
plt.show()
