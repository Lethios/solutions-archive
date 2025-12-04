# https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/

class Solution:
    def numberOfSubstrings(self, S: str) -> int:
        len_s = len(S)
        init = int(len_s ** 0.5) + 1

        zeros = deque(i for i, c in enumerate(S) if c == "0")
        zeros.append(len_s)

        ans = 0

        for i in range(len_s):
            while zeros and zeros[0] < i:
                zeros.popleft()

            prev = i

            for num_zeros, cur in enumerate(zeros):
                if num_zeros >= init:
                    break

                min_length = max(prev - i + 1, num_zeros * num_zeros + num_zeros)
                max_length = cur - i
                ans += max(max_length - min_length + 1, 0)

                prev = cur

        return ans
