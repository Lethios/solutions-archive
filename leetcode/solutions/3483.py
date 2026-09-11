# https://leetcode.com/problems/unique-3-digit-even-numbers/

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        count = [0] * 10

        for d in digits:
            count[d] += 1

        res = 0

        for i in range(1, 10):
            if count[i] == 0:
                continue
            
            count[i] -= 1

            for j in range(0, 10):
                if count[j] == 0:
                    continue
                
                count[j] -= 1

                for last in range(0, 10, 2):
                    if count[last] > 0:
                        res += 1

                count[j] += 1

            count[i] += 1

        return res
