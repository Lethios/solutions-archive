# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for row in range(m):
            for col in range(n):
                if row == col == 0:
                    continue

                if row - 1 >= 0 and col - 1 >= 0:
                    grid[row][col] += min(grid[row - 1][col], grid[row][col - 1])

                if row == 0:
                    grid[row][col] += grid[row][col - 1]

                if col == 0:
                    grid[row][col] += grid[row - 1][col]

        return grid[m - 1][n - 1]
