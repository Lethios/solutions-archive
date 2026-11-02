# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

import numpy as np

class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums, n = np.array(nums), len(nums)
        mid = np.partition(nums, n // 2)[n // 2]
        return int(sum(abs(num - mid) for num in nums))
