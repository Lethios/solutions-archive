# https://projecteuler.net/problem=40

def champernowne_constant(n):
    constant = "0."
    count = 1

    while len(constant) < n + 2:
        constant += str(count)
        count += 1

    return constant

frac = champernowne_constant(1000000)
product = int(frac[2]) * int(frac[11]) * int(frac[101]) * int(frac[1001]) * int(frac[10001]) * int(frac[100001]) * int(frac[1000001])

print(product)
# 210
