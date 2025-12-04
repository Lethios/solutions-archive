# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        len_n, i_list = len(nums), [0] * len(nums)
        l, r = 0, len_n - 1

        for i in reversed(range(len_n)):
            if abs(nums[l]) > abs(nums[r]):
                i_list[i] = abs(nums[l]) ** 2
                l += 1
            else:
                i_list[i] = abs(nums[r]) ** 2
                r -= 1
        
        return i_list
