# https://projecteuler.net/problem=10

def eratosthenes_sieve(limit):
    prime_list = [True] * (limit + 1)
    prime_list[0], prime_list[1] = False, False

    prime_sum = 0

    for num, prime in enumerate(prime_list):
        if prime:
            prime_sum += num
            for i in range(num * 2, limit + 1, num):
                prime_list[i] = False

    return prime_sum

print(eratosthenes_sieve(2000000))
# 142913828922
