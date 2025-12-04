# https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        land_set = set()
        grid_len = (len(grid), len(grid[0]))
        for m, row in enumerate(grid):
            for n, num in enumerate(row):
                if num == "1":
                    land_set.add((m, n))

        if len(land_set) == 0:
            return 0
        if len(land_set) == 1:
            return 1

        island = 0
        while len(land_set) > 0:
            i, j = land_set.pop()
            queue = deque([(i, j)])

            while queue:
                m, n = queue.popleft()

                if m + 1 < grid_len[0] and grid[m + 1][n] == "1":
                    grid[m + 1][n] = "0"
                    land_set.discard((m + 1, n))
                    queue.append((m + 1, n))
                if m - 1 >= 0 and grid[m - 1][n] == "1":
                    grid[m - 1][n] = "0"
                    land_set.discard((m - 1, n))
                    queue.append((m - 1, n))
                if n + 1 < grid_len[1] and grid[m][n + 1] == "1":
                    grid[m][n + 1] = "0"
                    land_set.discard((m, n + 1))
                    queue.append((m, n + 1))
                if n - 1 >= 0 and grid[m][n - 1] == "1":
                    grid[m][n - 1] = "0"
                    land_set.discard((m, n - 1))
                    queue.append((m, n - 1))
            
            island += 1
        
        return island
