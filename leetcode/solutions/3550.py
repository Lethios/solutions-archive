# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            num_sum = 0
            temp = num

            while temp > 0:
                num_sum += temp % 10
                temp //= 10

            if num_sum == i:
                return i

        return -1
