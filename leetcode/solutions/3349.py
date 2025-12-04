# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        cur_len, prev_len, max_len = 1, 0, 0

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur_len += 1
            else:
                prev_len = cur_len
                cur_len = 1
            maxLen = max(max_len, max(cur_len >> 1, min(prev_len, cur_len)))
            if maxLen >= k:
                return True

        return False
