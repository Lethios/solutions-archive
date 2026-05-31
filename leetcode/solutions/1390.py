# https://leetcode.com/problems/four-divisors/

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0

        for num in nums:
            curr_sum = 0
            count = 0

            for i in range(1, int(num**0.5) + 1):
                if num % i == 0:
                    curr_sum += i
                    count += 1

                    curr_sum += num // i
                    count += 1

                    if count > 4:
                        break
            
            if count == 4:
                res += curr_sum

        return res
