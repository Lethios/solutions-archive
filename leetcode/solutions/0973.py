# https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for point in points:
            x, y = point
            distance = (x ** 2) + (y ** 2)

            if len(max_heap) < k:
                heapq.heappush(max_heap, (-distance, [x, y]))
            else:
                if -distance > max_heap[0][0]:
                    heapq.heapreplace(max_heap, (-distance, [x, y]))

        return [point[1] for point in max_heap]
