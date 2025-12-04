# https://projecteuler.net/problem=4

def largest_palindrome(digit):
    largest = 0
    start = pow(10, digit) - 1
    end = pow(10, digit - 1) - 1

    for i in range(start, end, -1):
        for j in range(i, end, -1):
            num = i * j
            if str(num) == str(num)[::-1] and num > largest:
                largest = num

    return largest

print(largest_palindrome(3))
# 906609
