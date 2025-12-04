# https://projecteuler.net/problem=16

def power_digit_sum(base, power):
    power_num = str(int(pow(base, power)))
    power_sum = 0

    for index in range(0, len(power_num)):
        power_sum += int(power_num[index])

    return print(power_sum)

power_digit_sum(2, 1000)
# 1366
