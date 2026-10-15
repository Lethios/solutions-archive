# https://leetcode.com/problems/koko-eating-bananas/

import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)

        def compute_k(rate):
            return sum(math.ceil(num / rate) for num in piles)

        while left < right:
            mid = (left + right) // 2

            k = compute_k(mid)

            if k <= h:
                right = mid
                continue

            left = mid + 1

        return left
