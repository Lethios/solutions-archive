# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        kv = {"(": ")", "[": "]", "{": "}"}

        for char in s:
            if char in kv:
                stack.append(char)
            elif stack:
                if kv[stack[-1]] != char:
                    return False

                stack.pop()
            else:
                return False

        return len(stack) == 0
