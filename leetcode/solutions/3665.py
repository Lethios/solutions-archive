# https://leetcode.com/problems/twisted-mirror-path-count/

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        CONST = pow(10, 9) + 7
        m, n = len(grid), len(grid[0])

        dp = [[(0, 0) for _ in range(n)] for _ in range(m)]
        dp[0][0] = (1, 1)

        def paths(i: int, j: int) -> tuple[int, int]:
            a, b = 0, 0

            if 0 <= i - 1 < m:
                a = dp[i - 1][j][0]

            if 0 <= j - 1 < n:
                b = dp[i][j - 1][1]

            return (b, a)

        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue

                x, y = paths(i, j)

                if grid[i][j] == 0:
                    dp[i][j] = ((x + y) % CONST, (x + y) % CONST)
                else:
                    dp[i][j] = (x, y)

        return dp[-1][-1][0] % CONST
