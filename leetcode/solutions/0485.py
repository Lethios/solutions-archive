# https://leetcode.com/problems/max-consecutive-ones/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = longest = 0
        for char in nums:
            count = count + 1 if char == 1 else 0
            longest = count if count > longest else longest

        return longest
