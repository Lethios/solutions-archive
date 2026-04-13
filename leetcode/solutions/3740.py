# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        arr = [[] for _ in range(len(nums) + 1)]
        min_dist = 10**8

        for i, num in enumerate(nums):
            arr[num].append(i)

            if len(arr[num]) > 3:
                arr[num].pop(0)

            if len(arr[num]) == 3:
                min_dist = min(min_dist, 2 * (arr[num][2] - arr[num][0]))

        return min_dist if min_dist != 10**8 else -1
