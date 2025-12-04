# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        point = k = 0
        for num in nums:
            if num != val:
                nums[point] = num
                point += 1
                k += 1

        return k
