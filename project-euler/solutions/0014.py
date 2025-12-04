# https://projecteuler.net/problem=14

memo = {1: 0}

LONGEST_CHAIN = 0
LONGEST_CHAIN_NUMBER = 0

def collatz_chain(number):
    if number in memo:
        return memo[number]

    if number % 2 == 0:
        next_number = number // 2        
    else:
        next_number = 3 * number + 1   

    memo[number] = 1 + collatz_chain(next_number)
    return memo[number]

for i in range(2, 1000000):
    chain = collatz_chain(i)

    if chain > LONGEST_CHAIN:
        LONGEST_CHAIN = chain
        LONGEST_CHAIN_NUMBER = i

print(LONGEST_CHAIN_NUMBER)
# 837799
