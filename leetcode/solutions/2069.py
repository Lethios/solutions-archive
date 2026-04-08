# https://leetcode.com/problems/walking-robot-simulation-ii/

class Robot:

    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.current_loc = (0, 0)

        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.curr_dir = 1

        self.perimeter = 2 * (self.width + self.height - 2)

    def step(self, num: int) -> None:
        num %= self.perimeter

        if num == 0:
            num = self.perimeter
        
        for i in range(num):
            new_loc = (
                self.current_loc[0] + self.directions[self.curr_dir][0],
                self.current_loc[1] + self.directions[self.curr_dir][1],
            )

            while (
                new_loc[0] < 0
                or new_loc[1] < 0
                or new_loc[0] >= self.width
                or new_loc[1] >= self.height
            ):
                self.curr_dir = (self.curr_dir - 1) % 4

                new_loc = (
                    self.current_loc[0] + self.directions[self.curr_dir][0],
                    self.current_loc[1] + self.directions[self.curr_dir][1],
                )

            self.current_loc = new_loc

    def getPos(self) -> List[int]:
        return list(self.current_loc)

    def getDir(self) -> str:
        word_dir = {(0, 1): "North", (1, 0): "East", (0, -1): "South", (-1, 0): "West"}

        return word_dir[self.directions[self.curr_dir]]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
