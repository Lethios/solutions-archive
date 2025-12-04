# https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = sum = max_sum = 0
        n = len(nums)

        for r in range(k):
            sum += nums[r]
        max_sum = sum

        for r in range(k, n):
            sum += nums[r] - nums[l]
            l += 1
            max_sum = sum if sum > max_sum else max_sum

        return max_sum / k
