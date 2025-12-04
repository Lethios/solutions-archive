# https://projecteuler.net/problem=24

from itertools import permutations

digit_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
permutation_list = list(permutations(digit_list))

number = ""
for digit in permutation_list[999999]:
    number += str(digit)

print(number)
