# https://leetcode.com/problems/sum-of-squares-of-special-elements/

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res, n = 0, len(nums)

        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                res += nums[i - 1] ** 2

                if i != n // i:
                    res += nums[n // i - 1] ** 2

        return res
