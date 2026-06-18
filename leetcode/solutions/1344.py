# https://leetcode.com/problems/angle-between-hands-of-a-clock/

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        min_ratio = minutes / 60

        deg_min = 360 * min_ratio
        deg_hr = (hour * 30 + (30 * min_ratio)) % 360

        res = abs(deg_min - deg_hr)

        return min(res, 360 - res) 
