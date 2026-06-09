// https://leetcode.com/problems/maximum-total-subarray-value-i/

impl Solution {
    pub fn max_total_value(nums: Vec<i32>, k: i32) -> i64 {
        let mut max: i32 = nums[0];
        let mut min: i32 = nums[0];

        for num in nums {
            if num > max {
                max = num;
            }

            if num < min {
                min = num;
            }
        }

        ((max - min) as i64 * k as i64)
    }
}
