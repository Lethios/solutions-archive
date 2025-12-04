# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        temp = [words[0]]
        current = words[0]

        for word in words[1:]:
            if len(word) == len(current) and sorted(word) == sorted(current):
                continue

            temp.append(word)
            current = word
        words = temp

        return words
