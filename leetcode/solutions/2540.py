# https://leetcode.com/problems/minimum-common-value/

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        res = sorted(list(set(nums1) & set(nums2)))
        return res[0] if len(res) > 0 else -1
