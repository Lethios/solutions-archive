# https://leetcode.com/problems/check-if-array-is-good/

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        nums.sort()

        return [*[i for i in range(1, n)], *[n - 1]] == nums
