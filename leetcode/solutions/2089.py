# https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        idx, cnt = -1, 0

        for num in nums:
            if num < target:
                idx += 1
            elif num == target:
                cnt += 1

        return [i for i in range(idx + 1, idx + 1 + cnt)]
