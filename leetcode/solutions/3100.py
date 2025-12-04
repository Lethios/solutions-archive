# https://leetcode.com/problems/water-bottles-ii/

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        numBottles -= 1

        D = (2 * numExchange - 3) ** 2 + 8 * numBottles
        res = int((-(2 * numExchange - 3) + D ** 0.5) / 2)

        return numBottles + res + 1
