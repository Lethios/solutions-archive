# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for fix in range(len(nums)):
            if fix > 0 and nums[fix] == nums[fix - 1]:
                continue

            i = fix + 1
            j = len(nums) - 1

            while i < j:
                sum_n = nums[fix] + nums[i] + nums[j]

                if sum_n > 0:
                    j -= 1
                elif sum_n < 0:
                    i += 1
                else:
                    ans.append([nums[fix], nums[i], nums[j]])
                    i += 1

                    while nums[i] == nums[i - 1] and i < j:
                        i += 1

        return ans
