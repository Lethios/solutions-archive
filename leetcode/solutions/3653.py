# https://leetcode.com/problems/xor-after-range-multiplication-queries-i/

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for query in queries:
            l, r, k, v = query
            idx = l

            while idx <= r:
                nums[idx] = (nums[idx] * v) % (10**9 + 7)
                idx += k

        res = 0
        for num in nums:
            res ^= num

        return res
