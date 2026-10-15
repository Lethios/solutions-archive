# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = 0

        for i in range(len(nums)):
            hset = set()

            for j in range(i, len(nums)):
                hset.add(nums[j])
                res += len(hset) ** 2

        return res
