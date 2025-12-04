# https://leetcode.com/problems/water-bottles/

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = count = numBottles
        while empty >= numExchange:
            full = empty // numExchange
            count += full
            empty = empty % numExchange + full

        return count
