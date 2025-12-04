# https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        count, prev = 0, -float("inf")

        for num in nums:
            current = min(max(num - k, prev + 1), num + k)
            if current > prev:
                count += 1
                prev = current

        return count
