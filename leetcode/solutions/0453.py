# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_num = min(nums)
        return sum(num - min_num for num in nums)
