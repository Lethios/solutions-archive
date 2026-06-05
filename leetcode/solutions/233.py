# https://leetcode.com/problems/number-of-digit-one/

from functools import lru_cache

@lru_cache
def dfs(string: str, idx: int, tight: bool, digit_count: int):
    if idx == len(string):
        return digit_count
    
    lower_bound = 0
    upper_bound = ord(string[idx]) - ord("0") if tight else 9

    res = 0

    for digit in range(lower_bound, upper_bound + 1):
        res += dfs(string, idx + 1, tight and digit == upper_bound, digit_count + 1 if digit == 1 else digit_count)
    
    return res

class Solution:
    def countDigitOne(self, n: int) -> int:
        return dfs(str(n), 0, True, 0)
