# https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)

        for row in range(1, n):
            for col in range(n):
                a = matrix[row - 1][col - 1] if col - 1 >= 0 else float("inf")
                b = matrix[row - 1][col]
                c = matrix[row - 1][col + 1] if col + 1 < n else float("inf")

                matrix[row][col] += min(a, b, c)

        return min(matrix[n - 1])
