# https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1_list = version1.split(".")
        ver2_list = version2.split(".")

        for i, j in itertools.zip_longest(ver1_list, ver2_list, fillvalue="0"):
            print(i, j)
            if int(i) < int(j):
                return -1
            if int(i) > int(j):
                return 1

        return 0
