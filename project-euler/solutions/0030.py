# https://projecteuler.net/problem=30

fifth_power_numbers = []
FIFTH_POWER_NUMBERS_SUM = 0

for i in range(2, 1000000):
    FIFTH_POWER = 0

    for index in range(0, len(str(i))):
        FIFTH_POWER += pow(int(str(i)[index]), 5)

    if FIFTH_POWER == i:
        fifth_power_numbers.append(i)

for number in fifth_power_numbers:
    FIFTH_POWER_NUMBERS_SUM += number

print(FIFTH_POWER_NUMBERS_SUM)
# 443839
