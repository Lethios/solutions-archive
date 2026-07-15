# https://leetcode.com/problems/gcd-of-odd-and-even-sums/

class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_odd = n * (2 + (n - 1) * 2) // 2
        sum_even = n * (4 + (n - 1) * 2) // 2

        return gcd(sum_odd, sum_even)
