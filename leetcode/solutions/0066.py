# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in reversed(range(len(digits))):
            if i == len(digits) - 1:
                digits[i] += 1

            digits[i] += carry
            carry = digits[i] // 10
            digits[i] = digits[i] % 10

        if carry > 0:
            l = [carry]
            l.extend(digits)
            return l

        return digits
