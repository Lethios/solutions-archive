# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        spell_count = {}
        for p in power:
            spell_count[p] = spell_count.get(p, 0) + 1

        sorted_power = sorted(spell_count.keys())
        dp = [0] * len(sorted_power)

        for i in range(len(sorted_power)):
            prev_best = 0
           
            j = i - 1
            while j >= 0 and sorted_power[j] >= sorted_power[i] - 2:
                j -= 1
            if j >= 0:
                prev_best = dp[j]

            dp[i] = max(prev_best + sorted_power[i] * spell_count[sorted_power[i]], dp[i-1])

        return dp[-1] 
