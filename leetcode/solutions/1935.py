# https://leetcode.com/problems/maximum-number-of-words-you-can-type/

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        invalid = set(letter for letter in brokenLetters)
        counter = 0

        word_list = text.split(" ")
        for word in word_list:
            for letter in word:
                if letter in invalid:
                    counter += 1
                    break

        return len(word_list) - counter
