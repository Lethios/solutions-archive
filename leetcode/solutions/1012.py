# https://leetcode.com/problems/numbers-with-repeated-digits/

from functools import cache

string = ""

@cache
def dfs(idx: int, tight: bool, leading: bool, seen: int):
    if idx == len(string):
        return 1

    lb = 0
    ub = ord(string[idx]) - ord("0") if tight else 9

    res = 0

    for digit in range(lb, ub + 1):
        new_tight = tight and digit == ub
        new_leading = leading and digit == 0
        new_seen = seen

        if not new_leading:
            if new_seen & (1 << digit):
                continue
            else:
                new_seen |= 1 << digit

        res += dfs(idx + 1, new_tight, new_leading, new_seen)

    return res


class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        global string

        string = str(n)

        dfs.cache_clear()

        return n - dfs(0, True, True, 0) + 1
