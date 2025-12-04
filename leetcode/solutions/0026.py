# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        current, k = 0, 1
        for scout, num in enumerate(nums, start=1):
            if num != nums[current]:
                current += 1
                nums[current] = num
                k += 1

        return k
