# https://leetcode.com/problems/kth-largest-element-in-a-stream/

import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.k_largest = nums

        heapq.heapify(self.k_largest)

        while len(self.k_largest) > self.k:
            heapq.heappop(self.k_largest)

    def add(self, val: int) -> int:
        heapq.heappush(self.k_largest, val)
        
        while len(self.k_largest) > self.k:
            heapq.heappop(self.k_largest)

        return self.k_largest[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
