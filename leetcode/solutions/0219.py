# https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        unique = dict()

        for i, num in enumerate(nums):
            if num in unique and abs(i - unique[num]) <= k:
                return True
            else:
                unique[num] = i

        return False
