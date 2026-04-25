# https://leetcode.com/problems/sudoku-solver/

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]

        empty_coords = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty_coords.append((i, j))
                else:
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])

                    grid_idx = (i // 3) * 3 + (j // 3)
                    grids[grid_idx].add(board[i][j])

        def solve(idx):
            if idx == len(empty_coords):
                return True

            row, col = empty_coords[idx]
            valid_nums = {"1", "2", "3", "4", "5", "6", "7", "8", "9"} - (
                rows[row] | cols[col] | grids[(row // 3) * 3 + (col // 3)]
            )

            for num in valid_nums:
                board[row][col] = num

                rows[row].add(num)
                cols[col].add(num)

                grid_idx = (row // 3) * 3 + (col // 3)
                grids[grid_idx].add(num)

                if not solve(idx + 1):
                    board[row][col] = "."

                    rows[row].remove(num)
                    cols[col].remove(num)
                    grids[grid_idx].remove(num)
                else:
                    return True

            return False

        solve(0)
