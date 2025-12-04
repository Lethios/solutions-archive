# https://projecteuler.net/problem=43

from itertools import permutations

pandigital_list = list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
pandigital_property_list = []

for pandigital_number in pandigital_list:
    pandigital_num = ""
    for number in pandigital_number:
        pandigital_num += str(number)

    is_valid = True
    test_list = [1, 2, 3, 5, 7, 11, 13, 17]
    for i in range(1, 8):
        if int(pandigital_num[i] + pandigital_num[i + 1] + pandigital_num[i + 2]) % test_list[i] == 0:
            continue
        else:
            is_valid = False
            break
    
    if is_valid:
        pandigital_property_list.append(int(pandigital_num))

sum = 0
for num in pandigital_property_list:
    sum += num

print(sum)
# 16695334890
