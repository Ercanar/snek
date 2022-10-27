#!/usr/bin/env python3

import numpy
import random as ran

cube = [1, 2, 3, 4, 5, 6]
wurf = []

tempwurf = [ran.choice(cube) for _ in range(5)]

print(tempwurf)
b = input("Welchen behalten? ")
wurf += [tempwurf[i] for i in map(lambda x: int(x) - 1, b.split(" "))]
print(wurf)
