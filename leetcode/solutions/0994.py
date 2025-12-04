# https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        grid_dim = (len(grid), len(grid[0]))
        queue = deque()
        fresh = 0
        for m, row in enumerate(grid):
            for n, column in enumerate(row):
                if column == 2:
                    queue.append((m, n))
                elif column == 1:
                    fresh += 1
        
        if not queue and fresh > 0:
            return -1
        if not queue:
            return 0

        change, mins = True, -1

        while queue:
            for i in range(len(queue)):
                m, n = queue.popleft()

                if m + 1 < grid_dim[0] and grid[m + 1][n] == 1:
                    grid[m + 1][n] = 2
                    queue.append((m + 1, n))
                    fresh -= 1

                if m - 1 >= 0 and grid[m - 1][n] == 1:
                    grid[m - 1][n] = 2
                    queue.append((m - 1, n))
                    fresh -= 1

                if n + 1 < grid_dim[1] and grid[m][n + 1] == 1:
                    grid[m][n + 1] = 2
                    queue.append((m, n + 1))
                    fresh -= 1

                if n - 1 >= 0 and grid[m][n - 1] == 1:
                    grid[m][n - 1] = 2
                    queue.append((m, n - 1))
                    fresh -= 1

            mins += 1
        
        return mins if fresh == 0 else -1
