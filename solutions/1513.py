# https://leetcode.com/problems/number-of-substrings-with-only-1s/

class Solution:
    def numSub(self, s: str) -> int:
        count = substrings = 0

        for i, num in enumerate(s):
            if num == "1":
                count += 1
            else:
                substrings += (count * (count + 1)) // 2
                count = 0

        substrings += (count * (count + 1)) // 2

        return substrings % (10**9 + 7)

