# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        count, len_s, recent = 0, len(s), symbol_dict[s[0]]

        for char in s:
            current = symbol_dict[char]

            if current > recent:
                count += ( current - (2 * recent))
                recent = current
                continue

            count += current
            recent = current
        
        return count
