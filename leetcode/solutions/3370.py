# https://leetcode.com/problems/smallest-number-with-all-set-bits/

class Solution:
    def smallestNumber(self, n: int) -> int:
        len_b, ans = n.bit_length(), 1
        while ans - 1 < n:
            ans <<= 1
        
        return ans - 1
