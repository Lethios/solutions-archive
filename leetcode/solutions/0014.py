# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        len_strs, len_strs_word = len(strs), len(strs[0])
        current = ""

        if len_strs == 0:
            return ""
        if len_strs_word == 0:
            return ""
        
        for i in range(len_strs_word):
            for j in range(1, len_strs):
                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    return strs[0][:i]
        
        return strs[0]
