# https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0] = 1 - obstacleGrid[0][0]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1 or i == j == 0:
                    continue

                top_sum = dp[i - 1][j] if i > 0 else 0
                left_sum = dp[i][j - 1] if j > 0 else 0

                dp[i][j] = top_sum + left_sum

        return dp[m - 1][n - 1]
