# https://projecteuler.net/problem=29

distinct_terms = set()

for i in range(2, 101):
    for j in range(2, 101):
        num = pow(i, j)
        distinct_terms.add(num)

print(len(distinct_terms))
# 9183
