# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_count, magazine_count = Counter(ransomNote), Counter(magazine)

        return note_count <= magazine_count
