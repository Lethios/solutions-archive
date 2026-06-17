# https://leetcode.com/problems/process-string-with-special-operations-ii/

class Solution:
    def processStr(self, s: str, k: int) -> str:
        str_len = 0
        len_arr = []

        for char in s:
            match char:
                case "*":
                    str_len = max(str_len - 1, 0)
                case "#":
                    str_len *= 2
                case "%":
                    pass
                case _:
                    str_len += 1

            len_arr.append(str_len)

        if k >= str_len:
            return "."

        for i in reversed(range(len(s))):
            char = s[i]

            match char:
                case "*":
                    continue
                case "#":
                    if k >= len_arr[i] // 2:
                        k -= len_arr[i] // 2
                case "%":
                    k = len_arr[i] - 1 - k
                case _:
                    if k == len_arr[i] - 1:
                        return char
