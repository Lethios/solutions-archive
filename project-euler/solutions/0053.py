# https://projecteuler.net/problem=53

from math import comb

ans_count = 0

for n in range(1, 101):
    for r in range(1, n):
        if comb(n, r) > 1_000_000:
            ans_count += 1

print(ans_count)
# 4075
