# https://projecteuler.net/problem=48

def power_sum_series(n):
    number_sum = 0

    for number in range(1, n + 1):
        number_sum += pow(number, number)

    return number_sum

print(str(power_sum_series(1000))[-10:])
# 9110846700
