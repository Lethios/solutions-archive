# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n, ans = len(nums), 0
        cur, prev = 1, 0

        nums.append(-(10**10))

        for i in range(n):
            if nums[i + 1] > nums[i]:
                cur += 1
            else:
                ans = max(ans, cur // 2, prev if prev < cur else cur)
                prev = cur
                cur = 1

        return ans
