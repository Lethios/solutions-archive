# https://projecteuler.net/problem=2

A = 4000000
x, y = 1, 2
SUM = 0

while y < A:
    if y % 2 == 0:
        SUM += y

    z, x = x, y
    y += z

print(SUM)
# 4613732
