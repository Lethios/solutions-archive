# https://leetcode.com/problems/shortest-path-in-binary-matrix/

from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        n = len(grid)

        queue = deque([(0, 0, 0)])
        grid[0][0] = 1

        dirs = [(1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]

        while queue:
            i, j, l = queue.popleft()

            if i == j == n - 1:
                return l + 1

            for d in dirs:
                ni, nj, nl = i + d[0], j + d[1], l + 1

                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 0:
                    queue.append((ni, nj, nl))
                    grid[ni][nj] = 1

        return -1
