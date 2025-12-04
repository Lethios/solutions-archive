# https://leetcode.com/problems/greatest-sum-divisible-by-three/

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        nums.sort()
        total_sum = sum(nums)

        reminder = total_sum % 3
        if reminder == 0:
            return total_sum

        num_mods = [x % 3 for x in nums]

        nums_with_reminder_of_one = [x[1] for x in zip(num_mods, nums) if x[0] == 1][
            0:2
        ]
        nums_with_reminder_of_two = [x[1] for x in zip(num_mods, nums) if x[0] == 2][
            0:2
        ]

        if reminder == 1:
            sum_1 = (
                (total_sum - nums_with_reminder_of_one[0])
                if nums_with_reminder_of_one
                else 0
            )
            sum_2 = (
                total_sum - sum(nums_with_reminder_of_two)
                if len(nums_with_reminder_of_two) == 2
                else 0
            )
        else:
            sum_1 = (
                (total_sum - sum(nums_with_reminder_of_one))
                if len(nums_with_reminder_of_one) == 2
                else 0
            )
            sum_2 = (
                (total_sum - nums_with_reminder_of_two[0])
                if nums_with_reminder_of_two
                else 0
            )

        return max(sum_1, sum_2)
