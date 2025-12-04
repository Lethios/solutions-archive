# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [list(permutation) for permutation in itertools.permutations(nums)]
