# https://leetcode.com/problems/minimum-cost-to-acquire-required-items/

class Solution:
    def minimumCost(
        self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int
    ) -> int:
        res = 0

        if cost1 + cost2 > costBoth:
            if need1 < need2:
                res += need1 * costBoth
                need2 -= need1

                if cost2 < costBoth:
                    res += need2 * cost2
                else:
                    res += need2 * costBoth
            else:
                res += need2 * costBoth
                need1 -= need2

                if cost1 < costBoth:
                    res += need1 * cost1
                else:
                    res += need1 * costBoth
        else:
            res += need1 * cost1
            res += need2 * cost2

        return res
