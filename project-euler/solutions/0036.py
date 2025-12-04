# https://projecteuler.net/problem=36

def is_palindrome(n):
    return str(n) == str(n)[::-1]

PALINDROME_LIST_SUM = 0

for number in range(1, 1000000):
    if is_palindrome(number):
        binary = bin(number)[2:]

        if is_palindrome(binary):
            PALINDROME_LIST_SUM += number

print(PALINDROME_LIST_SUM)
# 872187
