# https://leetcode.com/problems/count-the-number-of-special-characters-ii/

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        seen_upper = 0
        seen_lower = 0
        mask_invalid = 0

        for char in word:
            if ord(char) < 97:
                seen_upper |= 1 << (ord(char) - 65)
            else:
                if (seen_upper >> ord(char) - 97) & 1 == 1:
                    mask_invalid |= 1 << (ord(char) - 97)
                else:
                    seen_lower |= 1 << (ord(char) - 97)

        return ((seen_upper & seen_lower) & ~mask_invalid).bit_count()
