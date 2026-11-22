# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

class Solution:
    def checkString(self, s: str) -> bool:
        seen_b = False

        for char in s:
            if char == "b":
                seen_b = True
            else:
                if seen_b:
                    return False

        return True
