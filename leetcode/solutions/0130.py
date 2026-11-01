# https://leetcode.com/problems/surrounded-regions/description/

from collections import deque


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        m, n = len(board), len(board[0])

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        seen = set()

        for row in range(m):
            for col in range(n):
                if board[row][col] == "X" or (row, col) in seen:
                    continue

                queue = deque([(row, col)])
                s = {(row, col)}
                boundary = False

                while queue:
                    i, j = queue.popleft()

                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        boundary = True

                    for di, dj in dirs:
                        ni, nj = i + di, j + dj

                        if (
                            0 <= ni < m
                            and 0 <= nj < n
                            and board[ni][nj] == "O"
                            and (ni, nj) not in s
                        ):
                            queue.append((ni, nj))
                            s.add((ni, nj))

                seen.update(s)

                if not boundary:
                    for i, j in s:
                        board[i][j] = "X"
