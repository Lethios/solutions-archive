# https://leetcode.com/problems/calculate-digit-sum-of-a-string/

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        res = [int(s[i]) for i in range(len(s))]

        while len(res) > k:
            temp = []

            for i in range(len(res)):
                if i % k == 0:
                    temp.append(res[i])
                else:
                    temp[-1] += res[i]

            res = [int(d) for x in temp for d in str(x)]

        return "".join(str(x) for x in res)
