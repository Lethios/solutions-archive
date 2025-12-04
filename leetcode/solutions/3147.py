# https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n, ans = len(energy), float("-inf")

        for i in reversed(range(n - k)):
            energy[i] += energy[i + k]

        for i in range(n):
            ans = ans if ans > energy[i] else energy[i]

        return ans
