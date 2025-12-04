# https://leetcode.com/problems/earliest-time-to-finish-one-task/

class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        min_sum = math.inf
        for task in tasks:
            min_sum = sum(task) if sum(task) < min_sum else min_sum

        return min_sum
