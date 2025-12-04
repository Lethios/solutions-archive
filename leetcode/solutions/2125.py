# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = prev = 0
        for row in bank:
            val = row.count('1')
            if val:
                ans += prev * val
                prev = val
        return ans
