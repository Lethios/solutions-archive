# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l_pointer = r_pointer = 0

        for r_pointer in range(len(nums)):
            if nums[r_pointer] != 0:
                nums[l_pointer], nums[r_pointer] = nums[r_pointer], nums[l_pointer]
                l_pointer += 1
