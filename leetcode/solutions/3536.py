# https://leetcode.com/problems/maximum-product-of-two-digits/

class Solution:
    def maxProduct(self, n: int) -> int:
        nums = [0, 0]

        while n > 0:
            digit = n % 10

            if digit > nums[0]:
                nums[1], nums[0] = nums[0], digit
            elif digit > nums[1]:
                nums[1] = digit

            n //= 10

        return nums[0] * nums[1]
