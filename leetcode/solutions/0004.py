# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr_len = len(nums1) + len(nums2)
        middle_index = arr_len // 2
        
        i, j = 0, 0
        count = 0
        last, second_last = 0, 0

        while count <= middle_index:
            second_last = last
            if i >= len(nums1):
                last = nums2[j]
                j += 1
            elif j >= len(nums2):
                last = nums1[i]
                i += 1
            elif nums1[i] < nums2[j]:
                last = nums1[i]
                i += 1
            else:
                last = nums2[j]
                j += 1
            count += 1

        if arr_len % 2 == 0:
            return (last + second_last) / 2
        else:
            return last
