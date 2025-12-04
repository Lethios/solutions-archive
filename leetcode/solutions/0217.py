# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_set = set(nums)

        return len(unique_set) != len(nums)
