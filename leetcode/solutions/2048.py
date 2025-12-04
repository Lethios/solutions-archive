# https://leetcode.com/problems/next-greater-numerically-balanced-number/

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        while True:
            n += 1
            counter = Counter(str(n))
            if all(int(key) == val for key, val in counter.items()):
                return n
