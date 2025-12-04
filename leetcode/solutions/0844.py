# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def clean_string(string: str) -> str:
            stack = []

            for char in string:
                if char == "#":
                    if stack: stack.pop()
                else:
                    stack.append(char)

            return stack
        
        return clean_string(s) == clean_string(t)
