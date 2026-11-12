# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res = 1

        asc = desc = 1
        for i, j in pairwise(nums):
            if i < j:
                asc += 1
            else:
                res = max(res, asc)
                asc = 1

            if i > j:
                desc += 1
            else:
                res = max(res, desc)
                desc = 1

        return max(res, asc, desc)
