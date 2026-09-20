# https://leetcode.com/problems/reverse-degree-of-a-string/

class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i, char in enumerate(s):
            res += (123 - ord(char)) * (i + 1)

        return res
