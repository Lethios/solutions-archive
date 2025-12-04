# https://projecteuler.net/problem=63

count = 0

for power in range(1, 5000):
    for base in range(1, 10):
        if len(str(base ** power)) == 4299:
            print(count)
            exit(0)
        if len(str(base ** power)) == power:
            count += 1

print(count)
# 49
