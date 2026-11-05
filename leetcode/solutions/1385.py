# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        res = 0

        for i in arr1:
            valid = True

            for j in arr2:
                if abs(i - j) <= d:
                    valid = False
                    break

            if valid:
                res += 1

        return res
