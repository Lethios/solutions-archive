# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen, res = 0, []
        temp = 0

        for i in range(len(A)):
            if A[i] == B[i]:
                temp += 1
                res.append(temp)
                continue

            if seen & (1 << A[i]):
                temp += 1
            else:
                seen |= (1 << A[i])

            if seen & (1 << B[i]):
                temp += 1
            else:
                seen |= (1 << B[i])

            res.append(temp)

        return res
