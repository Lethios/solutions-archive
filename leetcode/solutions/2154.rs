// https://leetcode.com/problems/keep-multiplying-found-values-by-two/

impl Solution {
    pub fn find_final_value(nums: Vec<i32>, mut original: i32) -> i32 {
        let len: usize = nums.len();
        let mut index: usize = 0;

        loop {
            if index >= len {
                return original;
            }

            if nums[index] == original {
                original *= 2;
                index = 0;
                continue;
            }

            index += 1
        }

        0
    }
}
