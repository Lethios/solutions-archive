# https://projecteuler.net/problem=7

def eratosthenes_sieve(limit):
    prime_list = [True] * (limit + 1)
    prime_list[0], prime_list[1] = False, False
    count = 0

    for num, prime in enumerate(prime_list):
        if prime:
            count += 1
            for i in range(num * 2, limit + 1, num):
                prime_list[i] = False

        if count == 10001:
            return num

print(eratosthenes_sieve(2000000))
# 104743
