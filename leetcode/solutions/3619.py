# https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/

from collections import deque


class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        res = 0
        m, n = len(grid), len(grid[0])

        def bfs(i, j):
            queue = deque([(i, j)])
            island_sum = grid[i][j]
            grid[i][j] = 0

            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            while queue:
                i, j = queue.popleft()

                for d in dirs:
                    ni, nj = i + d[0], j + d[1]
                    if not 0 <= ni < m or not 0 <= nj < n:
                        continue

                    if grid[ni][nj] != 0:
                        queue.append((ni, nj))
                        island_sum += grid[ni][nj]
                        grid[ni][nj] = 0

            return island_sum

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and bfs(i, j) % k == 0:
                    res += 1

        return res
