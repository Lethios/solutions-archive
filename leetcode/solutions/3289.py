# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        visited, ans = set(), []
        for num in nums:
            if num not in visited:
                visited.add(num)
            else:
                ans.append(num)
        
        return ans
