# https://projecteuler.net/problem=5

from math import lcm
from functools import reduce

def smallest_number(limit):
    num_list = [0] * limit

    for i in range(0, limit):
        num_list[i] = i + 1

    LCM = reduce(lcm, num_list)
    return LCM

print(smallest_number(20))
# 232792560
