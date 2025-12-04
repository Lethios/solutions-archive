# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left, right, i = m - 1, len(nums1) - 1, n - 1
        
        while i >= 0:
            if left >= 0 and nums1[left] > nums2[i]:
                nums1[right] = nums1[left]
                left -= 1
            else:
                nums1[right] = nums2[i]
                i -= 1
            right -= 1
