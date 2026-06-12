# https://leetcode.com/problems/number-of-beautiful-integers-in-the-range/

from functools import cache


class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:

        @cache
        def dfs(idx, tight, count, rem, leading):
            if idx == len(string):
                if count == 0 and rem == 0:
                    return 1

                return 0

            lb = 0
            ub = ord(string[idx]) - ord("0") if tight else 9

            res = 0

            for digit in range(lb, ub + 1):
                if leading and digit == 0:
                    res += dfs(
                        idx + 1,
                        tight and digit == ub,
                        count,
                        rem,
                        leading and digit == 0,
                    )

                    continue

                temp_count = count
                temp_rem = (rem * 10 + digit) % k

                if digit % 2 == 0:
                    temp_count += 1
                else:
                    temp_count -= 1

                res += dfs(
                    idx + 1,
                    tight and digit == ub,
                    temp_count,
                    temp_rem,
                    leading and digit == 0,
                )

            return res

        string = str(high)
        high_count = dfs(0, True, 0, 0, True)

        dfs.cache_clear()

        string = str(low - 1)
        low_count = dfs(0, True, 0, 0, True)

        return high_count - low_count
