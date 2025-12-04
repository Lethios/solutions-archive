# https://projecteuler.net/problem=12

from math import isqrt

def triangle_number(term):
    return term * (term + 1) // 2

def divisor_check(number):
    divisors = 0

    for i in range(1, isqrt(number) + 1):
        if number % i == 0:
            if i != number:
                divisors += 2
            else:
                divisors = 1

    return divisors

REQUIRED_DIVISORS = 500

DIVISOR = 1
X = 0

while DIVISOR < REQUIRED_DIVISORS:
    X += 1
    NUM = triangle_number(X)
    DIVISOR = divisor_check(NUM)

print(NUM)
# 76576500
