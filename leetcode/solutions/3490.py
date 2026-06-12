from functools import cache


class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:

        @cache
        def dfs(idx, tight, prod, dsum, leading):
            if idx == len(string):
                if dsum != 0 and prod % dsum == 0:
                    return 1

                return 0

            lb = 0
            ub = ord(string[idx]) - ord("0") if tight else 9

            res = 0

            for digit in range(lb, ub + 1):
                new_prod = prod * digit
                new_dsum = dsum + digit

                if leading and digit == 0:
                    new_prod = prod
                    new_dsum = dsum

                res += dfs(
                    idx + 1,
                    tight and digit == ub,
                    new_prod,
                    new_dsum,
                    leading and digit == 0,
                )

            return res

        string = str(r)
        r_count = dfs(0, True, 1, 0, True)

        dfs.cache_clear()

        string = str(l - 1)
        l_count = dfs(0, True, 1, 0, True)

        return r_count - l_count
