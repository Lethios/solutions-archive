# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digits = [int(d) for d in s]

        while len(digits) > 2:
            digits = [(a + b) % 10 for a, b in pairwise(digits)]

        one, two = digits
        return one == two
