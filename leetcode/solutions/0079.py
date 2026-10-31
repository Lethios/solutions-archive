# https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        start = [[], []]
        seen = set()

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def search(i: int, j: int, idx: int) -> bool:
            seen.add((i, j))

            if idx == len(word) - 1:
                seen.remove((i, j))
                return True

            for di, dj in dirs:
                ni, nj = i + di, j + dj

                if (ni, nj) in seen:
                    continue

                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] == word[idx + 1]:
                    if search(ni, nj, idx + 1):
                        seen.remove((i, j))
                        return True

            seen.remove((i, j))
            return False

        freq_check = 0

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    freq_check += 1
                    start[0].append((i, j))

                if board[i][j] == word[-1]:
                    freq_check -= 1
                    start[1].append((i, j))

        if freq_check > 0:
            word = word[::-1]
            start = start[1]
        else:
            start = start[0]

        for i, j in start:
            if board[i][j] == word[0] and search(i, j, 0):
                return True

        return False
