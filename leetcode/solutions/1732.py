# https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0

        alt = 0
        for diff in gain:
            alt += diff
            res = max(res, alt)

        return res
