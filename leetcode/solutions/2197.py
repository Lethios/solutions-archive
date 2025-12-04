# https://leetcode.com/problems/replace-non-coprime-numbers-in-array/

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []

        for num in nums:
            stack.append(num)
            
            while len(stack) >= 2 and gcd(stack[-1], stack[-2]) > 1:
                x = stack.pop()
                y = stack.pop()
                stack.append(lcm(x, y))

        return stack
