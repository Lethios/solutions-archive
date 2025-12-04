# https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in reversed(range(1, len(triangle))):
            for column in range(len(triangle[row]) - 1):
                triangle[row - 1][column] = triangle[row - 1][column] + min(triangle[row][column], triangle[row][column + 1])
        
        return triangle[0][0]
