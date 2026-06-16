# https://leetcode.com/problems/process-string-with-special-operations-i/

class Solution:
    def processStr(self, s: str) -> str:
        res = ""

        for char in s:
            match char:
                case "*":
                    res = res[:-1]
                case "#":
                    res += res
                case "%":
                    res = res[::-1]
                case _:
                    res += char

        return res
