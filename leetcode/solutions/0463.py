# https://leetcode.com/problems/island-perimeter/

from collections import deque


class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        def find():
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        return (i, j)

        start = find()
        queue = deque([start])
        grid[start[0]][start[1]] = -1

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while queue:
            i, j = queue.popleft()

            for d in dirs:
                ni, nj = i + d[0], j + d[1]

                if 0 <= ni < m and 0 <= nj < n:
                    if grid[ni][nj] == 1:
                        queue.append((ni, nj))
                        grid[ni][nj] = -1

                    elif grid[ni][nj] == 0:
                        res += 1
                else:
                    res += 1

        return res
