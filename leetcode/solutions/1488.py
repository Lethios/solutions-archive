# https://leetcode.com/problems/avoid-flood-in-the-city/

from bisect import bisect_right
from sortedcontainers import SortedList

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans, filled, empty = [-1]*len(rains), {}, SortedList()
        for i, lake in enumerate(rains):
            if lake == 0:
                empty.add(i)
                ans[i] = 1
            elif lake in filled:
                j = empty.bisect_right(filled[lake])
                if j == len(empty):
                    return []
                ans[empty[j]] = lake
                empty.pop(j)
                filled[lake] = i
            else:
                filled[lake] = i
        return ans
