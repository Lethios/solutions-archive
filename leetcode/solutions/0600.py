# https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/

from functools import cache

string = ""

@cache
def dfs(idx, tight, prev):
    if idx == len(string):
        return 1

    lb = 0
    ub = int(string[idx]) if tight else 1

    count = 0
    for digit in range(lb, ub + 1):
        if digit == 1 and prev == 1:
            continue

        count += dfs(idx + 1, tight and digit == ub, digit)

    return count


class Solution:
    def findIntegers(self, n: int) -> int:
        global string
        string = str(bin(n)[2:])

        dfs.cache_clear()

        return dfs(0, True, 0)
