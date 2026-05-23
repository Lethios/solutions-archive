// https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

impl Solution {
    pub fn check(nums: Vec<i32>) -> bool {
        let mut strike: i32 = 0;

        if nums[nums.len() - 1] > nums[0] {
            strike += 1;
        }
        
        for i in 1..nums.len() {
            if nums[i - 1] > nums[i] {
                strike += 1;
            }

            if strike > 1 {
                return false;
            }
        }

        true
    }
}
