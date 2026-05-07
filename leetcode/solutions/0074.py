# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        start, end = 0, m - 1
        candid_row = -1

        while start <= end:
            mid = (start + end) // 2

            if matrix[mid][0] < target:
                candid_row = mid
                start = mid + 1

            elif matrix[mid][0] > target:
                end = mid - 1

            else:
                return True

        start, end = 0, n - 1

        while start <= end:
            mid = (start + end) // 2

            if matrix[candid_row][mid] == target:
                return True

            elif matrix[candid_row][mid] < target:
                start = mid + 1

            elif matrix[candid_row][mid] > target:
                end = mid - 1

        return False
