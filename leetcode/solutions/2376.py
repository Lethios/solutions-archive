# https://leetcode.com/problems/count-special-integers/

from functools import cache

class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        string = str(n)
        
        @cache
        def dfs(idx: int, tight: bool, started: bool, seen: int) -> int:
            if idx == len(string):
                return 1

            lb = 0
            ub = int(string[idx]) if tight else 9

            res = 0

            for digit in range(lb, ub + 1):
                new_tight = tight and digit == ub
                new_started = started or digit != 0
                new_seen = seen

                if digit != 0 or started:
                    if new_seen & (1 << digit):
                        continue
                    else:
                        new_seen = seen | (1 << digit)

                res += dfs(idx + 1, new_tight, new_started, new_seen)

            return res

        return dfs(0, True, False, 0) - 1
