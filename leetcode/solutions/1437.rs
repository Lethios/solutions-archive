// https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

impl Solution {
    pub fn k_length_apart(nums: Vec<i32>, k: i32) -> bool {
        let mut prev: i32 = -1;

        for (index, bit) in nums.iter().enumerate() {
            if *bit == 1 {
                if prev == -1 {
                    prev = index as i32;
                } else {
                    if (index as i32) - prev - 1 < k {
                        return false;
                    }
                    prev = index as i32;
                }
            }
        }

        true
    }
}
