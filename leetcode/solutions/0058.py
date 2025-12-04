# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter, len_s = 0, len(s)

        for l in reversed(range(len_s)):
            if s[l] != " ":
                counter += 1
            elif s[l] == " " and counter == 0:
                continue
            else:
                return counter

        return counter
