# https://leetcode.com/problems/smallest-stable-index-i/

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        curr_max = -1
        max_list = [0] * n

        curr_min = float("inf")
        min_list = [0] * n

        for i in range(n):
            if nums[i] > curr_max:
                curr_max = nums[i]

            max_list[i] = curr_max

            if nums[n - i - 1] < curr_min:
                curr_min = nums[n - i - 1]

            min_list[n - i - 1] = curr_min

        for i, (num1, num2) in enumerate(zip(max_list, min_list)):
            if num1 - num2 <= k:
                return i

        return -1
