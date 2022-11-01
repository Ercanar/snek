#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import math

L = 20
offsetX = -10
offsetY = -10
s = 200
timesteps = 500
z = np.zeros((s, s, timesteps))

for t in range(timesteps):
    for y in range(s):
        for x in range(s):
            realX = (x*L/s + offsetX)
            realY = (y*L/s + offsetY)

            # always zero at boundaries
            if x == 0 or x == s - 1 or y == 0 or y == s - 1:
                z[x, y, t] = 0
            # base case: sine wave
            elif t == 0:
                z[x, y, t] = (
                    math.exp(-(realX ** 2 + realY ** 2) / 50) *
                    math.sin(0.2 * math.pi * realX) *
                    math.sin(0.2 * math.pi * realY)
                    )
            # second base case: weird hack
            elif t == 1:
                z[x, y, t] = z[x, y, 0] + 0.5 * (
                    z[x + 1, y, 0] +
                    z[x - 1, y, 0] -
                    z[x, y + 1, 0] +
                    z[x, y - 1, 0] -
                    2 * z[x, y, 0]
                )
            # all other timesteps
            else:
                z[x, y, t] = (
                    2 * z[x, y, t - 1] -
                    z[x, y, t - 2] + (
                        z[x + 1, y, t - 1] +
                        z[x - 1, y, t - 1] -
                        z[x, y + 1, t - 1] +
                        z[x, y - 1, t - 1] -
                        2 * z[x, y, t - 1]
                    ))

y = np.arange(s)
x = np.arange(s)
(x, y) = np.meshgrid(x, y)

# ax = plt.axes(projection="3d")
# ax.plot_surface(x, y, z[:, :, 10])

graphCount = 10
figure, ax = plt.subplots(
    ncols = graphCount,
    subplot_kw = dict(projection = "3d")
)

for t in range(graphCount):
    ax[t].plot_surface(x, y, z[:, :, t])

plt.show()
