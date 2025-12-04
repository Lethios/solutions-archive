# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = prev = 0

        for i in range(1, len(colors)):
            if colors[prev] != colors[i]:
                prev = i
            else:
                ans += (
                    neededTime[prev]
                    if neededTime[prev] < neededTime[i]
                    else neededTime[i]
                )
                if neededTime[prev] < neededTime[i]:
                    prev = i

        return ans
