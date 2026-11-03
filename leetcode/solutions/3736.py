# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = max(nums)
        return sum(m - num for num in nums)
