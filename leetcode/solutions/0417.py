# https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        r, c = len(heights), len(heights[0])
        a_set, p_set = set(), set()

        queue = deque()
        for i in range(r):
            if i == 0:
                for j in range(c):
                    queue.append((i, j))
            else:
                queue.append((i, 0))

        while queue:
            i, j = queue.popleft()
            p_set.add((i, j))

            for x, y in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                if 0 <= x < r and 0 <= y < c and (x, y) not in p_set and heights[i][j] <= heights[x][y]:
                    queue.append((x, y))

        queue.clear()
        for i in range(r):
            if i == r - 1:
                for j in range(c):
                    queue.append((i, j))
            else:
                queue.append((i, c - 1))

        while queue:
            i, j = queue.popleft()
            a_set.add((i, j))

            for x, y in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
                if 0 <= x < r and 0 <= y < c and (x, y) not in a_set and heights[i][j] <= heights[x][y]:
                    queue.append((x, y))

        return [[i, j] for i, j in p_set & a_set]
