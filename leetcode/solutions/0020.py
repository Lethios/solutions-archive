# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque

        stack = deque()

        valid = {
            "{":"}",
            "[":"]",
            "(":")"
        }  
        for pointer in range(len(s)):
            if s[pointer] in valid:
                stack.append(s[pointer])
            else:
                if stack and valid[stack[-1]] == s[pointer]:                
                    stack.pop()
                    continue
                else:
                    return False

        if stack:
            return False
        else:
            return True
