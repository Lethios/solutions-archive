# https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        stack = []
        ans = 0

        for n in nums:
            while stack and stack[-1] > n:
                stack.pop()

            if n == 0:
                continue

            if not stack or stack[-1] < n:
                ans += 1
                stack.append(n)

        return ans
