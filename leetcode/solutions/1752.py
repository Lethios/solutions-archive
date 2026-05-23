# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

class Solution:
    def check(self, nums: List[int]) -> bool:
        strike = 1 if nums[-1] > nums[0] else 0

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                strike += 1

            if strike > 1:
                return False

        return True
