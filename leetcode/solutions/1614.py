# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        res = curr = 0

        for char in s:
            if char == "(":
                curr += 1
                res = max(curr, res)
            elif char == ")":
                curr -= 1

        return res
