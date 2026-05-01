# https://leetcode.com/problems/rotate-function/

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)

        prev = sum([i * nums[i] for i in range(n)])
        max_sum = prev

        for k in range(1, n):
            curr = prev + total - (n * nums[n - k])
            max_sum = max(curr, max_sum)
            prev = curr 

        return max_sum
