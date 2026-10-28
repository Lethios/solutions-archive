# https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[0 for _ in range(n)] for _ in range(m)]
        res[0][0] = 1

        for row in range(m):
            for col in range(n):
                if row - 1 >= 0:
                    res[row][col] += res[row - 1][col]

                if col - 1 >= 0:
                    res[row][col] += res[row][col - 1]

        return res[m - 1][n - 1]
