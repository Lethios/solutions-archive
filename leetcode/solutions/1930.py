# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        first = [n] * 26
        last = [-1] * 26

        for i, char in enumerate(s):
            index = ord(char) - ord("a")
            first[index] = first[index] if first[index] < i else i
            last[index] = i

        ans = 0

        for c in range(26):
            L, R = first[c], last[c]

            if R - L < 2:
                continue

            seen = [False] * 26

            for i in range(L + 1, R):
                index = ord(s[i]) - ord("a")

                if not seen[index]:
                    seen[index] = True
                    ans += 1

        return ans
