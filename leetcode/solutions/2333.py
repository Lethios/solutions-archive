# https://leetcode.com/problems/minimum-sum-of-squared-difference/

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = [abs(i - j) for i, j in zip(nums1, nums2)]
        max_n = max(diff)
        k = k1 + k2

        buckets = [0] * (max_n + 1)

        for num in diff:
            buckets[num] += 1

        for i in reversed(range(1, max_n + 1)):
            if buckets[i] > 0 and k > 0:
                sub = min(buckets[i], k)
                buckets[i] -= sub
                buckets[i - 1] += sub
                k -= sub

            if k <= 0:
                break

        return sum((i**2) * num for i, num in enumerate(buckets))
