# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        long_set = set()
        longest = 0

        for r, char in enumerate(s):            
            if char not in long_set:
                long_set.add(char)
                longest = longest if r - l + 1 < longest else r - l + 1
            else:
                while char in long_set:
                    long_set.remove(s[l])
                    l += 1
                long_set.add(char)
        
        return longest
