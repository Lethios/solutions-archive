# https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]

        for i in range(1, n + 1):
            ans.append(ans[i & (i - 1)] + 1)
        
        return ans
