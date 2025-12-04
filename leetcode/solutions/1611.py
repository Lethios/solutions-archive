# https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        
        x = 0
        curr = 1
        while (curr * 2) <= n:
            curr *= 2
            x += 1

        return 2 ** (x + 1) - 1 - self.minimumOneBitOperations(n ^ curr)
