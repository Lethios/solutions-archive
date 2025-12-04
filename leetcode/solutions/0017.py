# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        num_comb = []
        for num in reversed(digits):
            temp = []
            if len(num_comb) == 0:
                temp = [f"{x}" for x in mapping[num]]
            else:
                temp = [f"{x}{y}" for x in mapping[num] for y in num_comb]
            num_comb = temp

        return num_comb
