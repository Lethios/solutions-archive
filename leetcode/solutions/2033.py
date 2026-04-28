# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])
        operations = 0

        arr = [grid[i][j] for i in range(m) for j in range(n)]
        arr.sort()

        median = arr[(m * n) // 2]

        for num in arr:
            temp = abs(median - num) / x

            if temp.is_integer():
                operations += int(temp)
            else:
                return -1

        return operations
