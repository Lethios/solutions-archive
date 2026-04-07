# https://leetcode.com/problems/walking-robot-simulation/

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        max_dist = 0
        curr_loc = (0, 0)

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_dir = 0

        obstacle_set = {tuple(o) for o in obstacles}

        for command in commands:
            match command:
                case -2:
                    curr_dir = (curr_dir - 1) % 4
                case -1:
                    curr_dir = (curr_dir + 1) % 4
                case _:
                    for i in range(command):
                        next_loc = (
                            curr_loc[0] + directions[curr_dir][0],
                            curr_loc[1] + directions[curr_dir][1],
                        )

                        if next_loc in obstacle_set:
                            break

                        curr_loc = next_loc
                        max_dist = max(
                            (curr_loc[0] ** 2) + (curr_loc[1] ** 2), max_dist
                        )

        return max_dist
