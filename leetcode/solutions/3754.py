# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        res = 0
        digit_sum = 0

        for digit in str(n):
            digit = ord(digit) - ord("0")

            if digit:
                res = res * 10 + digit
                digit_sum += digit

        return res * digit_sum
