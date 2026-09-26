# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        know = dict(knowledge)
        parts = []
        is_in_paren = False
        start = -1

        for i, char in enumerate(s):
            if char == "(":
                is_in_paren = True
                start = i
            elif char == ")":
                is_in_paren = False
                word = know.get(s[start + 1 : i], "?")
                parts.append(word)
            else:
                if not is_in_paren:
                    parts.append(s[i])

        return "".join(parts)
