// https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/

impl Solution {
    pub fn sum_and_multiply(n: i32) -> i64 {
        let mut res: i64 = 0;
        let mut digit_sum: i64 = 0;

        for digit in n.to_string().bytes() {
            digit = (digit - 0 as u8) as i64;

            if digit != 0 {
                res = res * 10 + digit;
                digit_sum += digit;
            }
        }

        res * digit_sum
    }
}
