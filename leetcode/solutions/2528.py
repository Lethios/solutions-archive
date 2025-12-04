# https://leetcode.com/problems/maximize-the-minimum-powered-city/

class Solution:
    def maxPower(self, stations, r, k):
        n = len(stations)
        diff = [0] * (n + 5)

        for i, j in enumerate(stations):
            diff[max(0, i - r)] += j
            diff[min(n - 1, i + r) + 1] -= j

        low, high = min(accumulate(diff[:n])), 2 * (10 ** 10)

        def check(mid):
            temp = diff[:] 
            curr, count = 0, 0

            for i in range(n):
                curr += temp[i]
                if curr < mid:
                    need = mid - curr
                    count += need
                    if count > k:
                        return False
                    curr = mid
                    temp[min(n - 1, i + 2 * r) + 1] -= need

            return True

        while low < high:
            mid = (low + high + 1) >> 1

            if check(mid):
                low = mid
            else:
                high = mid - 1

        return low
