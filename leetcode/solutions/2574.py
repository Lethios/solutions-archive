# https://leetcode.com/problems/left-and-right-sum-differences/

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)

        num_sum = 0
        left_sum = [0] * n
        for i in range(n):
            left_sum[i] = num_sum
            num_sum += nums[i]

        num_sum = 0
        right_sum = [0] * n
        for i in reversed(range(n)):
            right_sum[i] = num_sum
            num_sum += nums[i]

        return [abs(i - j) for i, j in zip(left_sum, right_sum)]
