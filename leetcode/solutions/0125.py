# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(char.lower() for char in s if char.isalnum())

        return clean == clean[::-1]
