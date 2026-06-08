from functools import cache

class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        string = ""
        MOD = pow(10, 9) + 7

        @cache
        def dfs(idx, tight, curr_sum):
            if idx == len(string):
                return 1 if min_sum <= curr_sum <= max_sum else 0

            lb = 0
            ub = ord(string[idx]) - ord("0") if tight else 9

            if curr_sum > max_sum:
                return 0

            res = 0
            for digit in range(lb, ub + 1):
                res = (res + dfs(idx + 1, tight and digit == ub, curr_sum + digit)) % MOD

            return res

        string = str(int(num1) - 1)
        num1_count = dfs(0, True, 0)

        dfs.cache_clear()

        string = num2
        num2_count = dfs(0, True, 0)

        return (num2_count - num1_count) % MOD
