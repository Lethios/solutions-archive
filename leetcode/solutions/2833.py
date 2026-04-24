# https://leetcode.com/problems/furthest-point-from-origin/

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        pos = temp = 0
        
        for move in moves:
            match move:
                case 'L':
                    pos -= 1
                case 'R':
                    pos += 1
                case _:
                    temp += 1
        
        return abs(pos) + temp
