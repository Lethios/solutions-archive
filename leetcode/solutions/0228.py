# https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        range_list = []

        for num in nums:
            if range_list and range_list[-1][1] == num - 1:
                range_list[-1][1] = num
            else:
                range_list.append([num, num])

        return [f"{x}->{y}" if x != y else f"{x}" for x, y in range_list]
