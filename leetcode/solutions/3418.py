import math


class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        dp = [
            [[-math.inf, -math.inf, -math.inf] for col in range(n)] for row in range(m)
        ]

        dp[0][0][0] = coins[0][0]
        dp[0][0][1] = dp[0][0][2] = 0

        for i in range(m):
            for j in range(n):
                for k in range(3):
                    if i > 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k] + coins[i][j])
                    if i > 0 and k > 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k - 1])
                    if j > 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k] + coins[i][j])
                    if j > 0 and k > 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i][j - 1][k - 1])

        return max(dp[m - 1][n - 1])
