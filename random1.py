#!/bin/python
## This program prints 1 to 10 numbers in a random order
import random
import numpy as np

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
np.random.shuffle(numbers)
r = range(0, 10, 1)
for x in r:
    print(numbers[x])

