# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        if len(words) != len(pattern):
            return False

        d1, d2 = {}, {}

        for letter, word in zip(pattern, words):
            if letter in d1 and d1[letter] != word:
                return False

            if word in d2 and d2[word] != letter:
                return False

            d1[letter] = word
            d2[word] = letter

        return True
