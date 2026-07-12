# https://leetcode.com/problems/rank-transform-of-an-array/

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        mapping = {}

        for rank, val in enumerate(sorted(set(arr)), 1):
            mapping[val] = rank

        return [mapping[x] for x in arr]
