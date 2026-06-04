# https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        waviness = 0

        for num in range(num1, num2 + 1):
            if num < 100:
                continue
            
            digits = []
            temp = num

            while temp > 0:
                digits.append(temp % 10)
                temp //= 10
            
            for i in range(1, len(digits) - 1):
                if digits[i - 1] < digits[i] > digits[i + 1] or digits[i - 1] > digits[i] < digits[i + 1]:
                    waviness += 1

        return waviness
