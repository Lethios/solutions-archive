# https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        temp = goal[0]
        
        for i, char in enumerate(s):
            if char == temp and s[i:] + s[:i] == goal:
                return True
        
        return False
