# https://leetcode.com/problems/find-triangular-sum-of-an-array/

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        len_n = len(nums)
        for i in range(len_n - 1):
            for j in range(len_n - 1 - i):
                nums[j] = (nums[j] + nums[j + 1]) % 10

        return nums[0]
