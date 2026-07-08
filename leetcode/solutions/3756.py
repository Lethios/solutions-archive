# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        res = []

        n = len(s)
        MOD = pow(10, 9) + 7

        prefix_sum = [0 for _ in range(n)]
        prefix_digit = [[0, 0] for _ in range(n)]
        prefix_sum[0] = prefix_digit[0][0] = int(s[0])
        prefix_digit[0][1] = 1

        MOD = pow(10, 9) + 7

        for i in range(1, n):
            digit = int(s[i])

            prefix_sum[i] = (prefix_sum[i - 1] + digit) % MOD

            prefix_digit[i][0] = prefix_digit[i - 1][0]
            prefix_digit[i][1] = prefix_digit[i - 1][1]

            if digit != 0:
                prefix_digit[i][0] = (prefix_digit[i - 1][0] * 10 + digit) % MOD
                prefix_digit[i][1] += 1

        for l, r in queries:
            if l == 0:
                digit_sum = prefix_sum[r]
                num = prefix_digit[r][0]
            else:
                digit_sum = (prefix_sum[r] - prefix_sum[l - 1]) % MOD

                right_count = prefix_digit[r][1] - prefix_digit[l - 1][1]

                num = (
                    prefix_digit[r][0]
                    - prefix_digit[l - 1][0] * pow(10, right_count, MOD)
                ) % MOD

            res.append((num * digit_sum) % MOD)
        
        return res
