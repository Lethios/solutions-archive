# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        l = len(columnTitle)
        res = 0

        for char in columnTitle:
            res += pow(26, l - 1) * (ord(char) - 64)
            l -= 1

        return res
