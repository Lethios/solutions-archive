# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        min_cost = 0
        freq_arr = [0] * (max(cost) + 1)

        for num in cost:
            freq_arr[num] += 1

        temp = 1
        for c_cost in reversed(range(len(freq_arr))):
            while freq_arr[c_cost] > 0:
                if temp % 3 == 0:
                    freq_arr[c_cost] -= 1
                    temp += 1
                    continue

                min_cost += c_cost
                freq_arr[c_cost] -= 1
                temp += 1

        return min_cost
