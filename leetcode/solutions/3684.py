# https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/

class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        return sorted(list(set(nums)), reverse=True)[:k]
