# https://leetcode.com/problems/separate-the-digits-in-an-array/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            if num <= 9:
                res.append(num)
            else:
                for digit in str(num):
                    res.append(int(digit))

        return res
