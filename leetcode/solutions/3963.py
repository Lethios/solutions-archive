# https://leetcode.com/problems/create-grid-with-exactly-one-path/

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res = []

        for i in range(m):
            row = []
            for j in range(n):
                if i == 0 or j == n - 1:
                    row.append(".")
                else:
                    row.append("#")

            res.append("".join(row))

        return res
