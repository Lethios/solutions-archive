# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        counter = 0

        for element in nums:
            if counter == 0:
                candidate = element
            
            counter = counter + 1 if element == candidate else counter - 1

        return candidate
