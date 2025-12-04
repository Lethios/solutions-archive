# https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        length = 0

        is_odd = False
        for value in counter.values():
            if value & 1:
                length += value - 1
                is_odd = True
            else:
                length += value

        return length + 1 if is_odd else length
