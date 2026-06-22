# https://leetcode.com/problems/maximum-number-of-balloons/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        res = float("inf")

        freq_dict = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}

        for char in text:
            if char in freq_dict:
                freq_dict[char] += 1

        return min(
            freq_dict["b"],
            freq_dict["a"],
            freq_dict["l"] // 2,
            freq_dict["o"] // 2,
            freq_dict["n"]
        )
