# https://leetcode.com/problems/stone-removal-game/

class Solution:
    def canAliceWin(self, n: int) -> bool:
        stone = 10

        while stone > 0:
            if n - stone < 0:
                return stone % 2 == 1

            n -= stone
            stone -= 1

        return False
