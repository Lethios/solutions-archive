# https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        skill_sum = [0] * n

        for i in range(1, n):
            skill_sum[i] = skill[i] + skill_sum[i - 1]

        total_time = skill[0] * mana[0]

        for i in range(1, m):
            max_time = skill[0] * mana[i]
            for j in range(1, n):
                d_time = (skill_sum[j] * mana[i - 1]) - (skill_sum[j - 1] * mana[i])
                if d_time > max_time:
                    max_time = d_time

            total_time += max_time

        return total_time + (skill_sum[-1] * mana[-1])
