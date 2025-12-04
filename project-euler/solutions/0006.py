# https://projecteuler.net/problem=6

def difference(limit):
    sum = (limit * (limit + 1)) // 2
    sum_square = sum * sum
    square_sum = (limit * (limit + 1) * (2 * limit + 1)) // 6

    diff = sum_square - square_sum
    return diff

print(difference(100))
# 25164150
