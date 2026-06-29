# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0

        for pattern in patterns:
            if pattern in word:
                res += 1

        return res
