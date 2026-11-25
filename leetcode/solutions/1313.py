# https://leetcode.com/problems/decompress-run-length-encoded-list/

class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        n, res = len(nums), []

        for i in range(0, n, 2):
            res.extend([nums[i + 1]] * nums[i])

        return res
