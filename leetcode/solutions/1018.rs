// https://leetcode.com/problems/binary-prefix-divisible-by-5/

impl Solution {
    pub fn prefixes_div_by5(nums: Vec<i32>) -> Vec<bool> {
        let mut ans: Vec<bool> = Vec::with_capacity(nums.len());
        let mut check: i32 = 0;

        for bit in nums {
            check = (bit + (check * 2)) % 5;
            ans.push(check == 0);
        }

        ans
    }
}
