# https://projecteuler.net/problem=1

X = 100000213
SUM = 0

for i in range(0, X):
    if (i % 3 == 0) or (i % 5 == 0):
        SUM += i

print(SUM)
# 233168
