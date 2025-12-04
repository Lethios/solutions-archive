# https://projecteuler.net/problem=3

def prime_factor(n):
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            n = n // i
        else:
            i += 1

    return n

print(prime_factor(600851475143))
# 6857
