# https://leetcode.com/problems/calculate-money-in-leetcode-bank/

class Solution:
    def totalMoney(self, n: int) -> int:
        weeks, days = divmod(n, 7)
        sum = 0
        if n > 7:
            for i in range(1, weeks + 1):
                sum += 7 * (2 * i + 6) // 2
        
        return sum + days * (2 * (weeks + 1) + days - 1) // 2
