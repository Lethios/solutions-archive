class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = [0] * 9
        cols = [0] * 9
        grids = [0] * 9

        empty_coords = set()

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    val = int(board[i][j])

                    rows[i] |= 1 << val
                    cols[j] |= 1 << val
                    grids[(i // 3) * 3 + (j // 3)] |= 1 << val
                else:
                    empty_coords.add((i, j))
        
        FULL = 0b1111111110

        def valid(row, col):
            return FULL & ~(rows[row] | cols[col] | grids[(row // 3) * 3 + (col // 3)])

        def solve():
            if not empty_coords:
                return True

            row, col = min(empty_coords, key=lambda coord: valid(coord[0], coord[1]).bit_count())
            grid_idx = (row // 3) * 3 + (col // 3)

            valid_num = valid(row, col)

            if not valid_num:
                return False
            
            empty_coords.remove((row, col))
            
            while valid_num:
                mask = valid_num & -valid_num
                valid_num ^= mask

                num = mask.bit_length() - 1

                board[row][col] = str(num)

                rows[row] |= mask
                cols[col] |= mask
                grids[grid_idx] |= mask

                if not solve():
                    board[row][col] = "."

                    rows[row] &= ~mask
                    cols[col] &= ~mask
                    grids[grid_idx] &= ~mask
                else:
                    return True

            empty_coords.add((row, col))
            return False

        solve()
