# https://leetcode.com/problems/minimum-xor-path-in-a-grid/

class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[set() for _ in range(n)] for _ in range(m)]

        for row in range(m):
            for col in range(n):
                if row == col == 0:
                    dp[0][0].add(grid[0][0])
                    continue

                if row > 0:
                    for num in dp[row - 1][col]:
                        dp[row][col].add(num ^ grid[row][col])

                if col > 0:
                    for num in dp[row][col - 1]:
                        dp[row][col].add(num ^ grid[row][col])

        return min(dp[-1][-1])
