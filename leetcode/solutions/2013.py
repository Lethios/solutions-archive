# https://leetcode.com/problems/detect-squares/

class DetectSquares:

    def __init__(self):
        self.point_freq = {}
        self.x_dict = {}

    def add(self, point: list[int]) -> None:
        point = tuple(point)

        if point not in self.point_freq:
            if point[0] not in self.x_dict:
                self.x_dict[point[0]] = []

            self.point_freq[point] = 0
            self.x_dict[point[0]].append(point[1])

        self.point_freq[point] += 1

    def count(self, point: list[int]) -> int:
        point = tuple(point)
        res = 0

        if point[0] not in self.x_dict:
            return 0

        for y in self.x_dict[point[0]]:
            l = abs(point[1] - y)

            if l == 0:
                continue

            left = ((point[0] - l, point[1]), (point[0] - l, y))
            right = ((point[0] + l, point[1]), (point[0] + l, y))

            if left[0] in self.point_freq and left[1] in self.point_freq:
                res += (
                    self.point_freq[left[0]]
                    * self.point_freq[left[1]]
                    * self.point_freq[(point[0], y)]
                )

            if right[0] in self.point_freq and right[1] in self.point_freq:
                res += (
                    self.point_freq[right[0]]
                    * self.point_freq[right[1]]
                    * self.point_freq[(point[0], y)]
                )

        return res
