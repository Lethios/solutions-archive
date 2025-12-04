# https://projecteuler.net/problem=20

from math import factorial as fac

def factorial_digit_sum(number):
    factorial = fac(number)
    num_sum = 0

    for index in range(0, len(str(factorial))):
        num_sum += int(str(factorial)[index])

    return num_sum

print(factorial_digit_sum(100))
# 648
