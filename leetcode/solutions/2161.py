# https://leetcode.com/problems/partition-array-according-to-given-pivot/

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lesser = []
        greater = []
        equal = []

        for num in nums:
            if num < pivot:
                lesser.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                equal.append(num)

        lesser.extend(equal)
        lesser.extend(greater)

        return lesser
