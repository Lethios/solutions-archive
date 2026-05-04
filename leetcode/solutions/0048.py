# https://leetcode.com/problems/rotate-image/

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        if n == 1:
            return

        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in range(n):
            for col in range(n // 2):
                matrix[row][col], matrix[row][n - col - 1] = (
                    matrix[row][n - col - 1],
                    matrix[row][col],
                )
