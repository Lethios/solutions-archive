# https://leetcode.com/problems/valid-triangle-number/

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        len_n, count = len(nums), 0

        for fix in reversed(range(2, len_n)):
            i, j = 0, fix - 1

            while i < j:
                if nums[i] + nums[j] > nums[fix]:
                    count += j - i
                    j -= 1
                else:                
                    i += 1
        
        return count
