# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_index = 0
        right_index = len(height) - 1
        max_area = 0

        while left_index < right_index:
            h = min(height[left_index], height[right_index])
            w = right_index - left_index
            max_area = max(max_area, h * w)

            if height[left_index] < height[right_index]:
                left_index += 1
            else:
                right_index -= 1

        return max_area
