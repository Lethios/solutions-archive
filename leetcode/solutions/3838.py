# https://leetcode.com/problems/weighted-word-mapping/

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = []

        for word in words:
            weight = 0

            for char in word:
                weight += weights[ord(char) - 97]

            weight %= 26
            res.append(chr(ord("z") - weight))

        res = "".join(res)

        return res
