# https://leetcode.com/problems/swim-in-rising-water/

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if n == 1:
            return 0
        else:
            min_heap = []

        heapq.heappush(min_heap, (grid[0][0], 0, 0))
        visited = {(0, 0)}

        while min_heap:
            val, i, j = heapq.heappop(min_heap)
            if i == j == n - 1:
                return val

            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < n and 0 <= y < n and (x, y) not in visited:
                    heapq.heappush(min_heap, (max(val, grid[x][y]), x, y))
                    visited.add((x, y))

        return -1
