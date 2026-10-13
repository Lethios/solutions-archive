# https://leetcode.com/problems/maximum-alternating-sum-of-squares/

import numpy as np

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        neg = len(nums) // 2
        res = np.partition(np.square(np.array(nums)), kth=neg)
        return int(np.sum(res[neg:]) - np.sum(res[:neg]))
