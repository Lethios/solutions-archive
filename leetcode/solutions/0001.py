# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i, num in enumerate(nums):
            diff = target - num
            
            if diff in num_dict:
                return [num_dict[diff], i]
            
            else:
                num_dict[num] = i

        return []
