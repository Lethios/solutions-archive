# https://leetcode.com/problems/count-the-number-of-special-characters-i/

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        bitmask_lower = 0
        bitmask_upper = 0

        for char in word:
            if ord(char) >= 97:
                bitmask_lower |= (1 << ord(char) - 97)
            else:
                bitmask_upper |= (1 << ord(char) - 65)
        
        return (bitmask_lower & bitmask_upper).bit_count()
