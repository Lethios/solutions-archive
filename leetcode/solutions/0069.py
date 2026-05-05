# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        left, right = 0, x // 2
        candid = -1

        while left <= right:
            mid = (left + right) // 2
            sqr = mid * mid

            if sqr == x:
                return mid

            elif sqr > x:
                right = mid - 1

            else:
                candid = max(candid, mid)
                left = mid + 1

        return candid
