# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/

class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_element = 100000

        for num in nums:
            digit_sum = 0
            temp = num

            while temp > 0:
                digit_sum += temp % 10
                temp //= 10

            min_element = min(min_element, digit_sum)

        return min_element
