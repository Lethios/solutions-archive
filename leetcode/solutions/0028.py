# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_n, len_h = len(needle), len(haystack)

        if len_n > len_h:
            return -1
        
        for i, char in enumerate(haystack):
            if char == needle[0] and haystack[i:i + len_n] == needle:
                return i
        
        return -1
