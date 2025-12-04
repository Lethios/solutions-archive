# https://leetcode.com/problems/trapping-rain-water-ii/

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        rows, columns = len(heightMap), len(heightMap[0])
        if rows < 3 or columns < 3:
            return 0

        heap = []
        for i in range(rows):
            for j in range(columns):
                if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1

        level, ans = 0, 0
        while heap:
            height, x, y = heapq.heappop(heap)
            level = height if height > level else level

            for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= i < rows and 0 <= j < columns and heightMap[i][j] != -1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))

                    if heightMap[i][j] < level:
                        ans += level - heightMap[i][j]
                    heightMap[i][j] = -1

        return ans
