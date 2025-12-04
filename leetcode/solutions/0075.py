# https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        color = [0, 0, 0]

        for num in nums:
            color[num] += 1

        index = 0
        for i in range(3):
            for j in range(color[i]):
                nums[index] = i
                index += 1
