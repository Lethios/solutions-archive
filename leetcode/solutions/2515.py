# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        left = right = startIndex

        for _ in range(n // 2 + 1):
            if words[left] == target:
                return min((left - startIndex + n) % n, n - (left - startIndex + n) % n)

            if words[right] == target:
                return min(
                    (right - startIndex + n) % n, n - (right - startIndex + n) % n
                )

            left = (left - 1 + n) % n
            right = (right + 1) % n

        return -1
