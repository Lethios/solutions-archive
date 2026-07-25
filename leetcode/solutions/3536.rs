// https://leetcode.com/problems/maximum-product-of-two-digits/

impl Solution {
    pub fn max_product(n: i32) -> i32 {
        let mut num1: i32 = 0;
        let mut num2: i32 = 0;

        let mut temp: i32 = n;

        while temp > 0 {
            let digit: i32 = temp % 10;

            if digit > num1 {
                num2 = num1;
                num1 = digit;
            } else if digit > num2 {
                num2 = digit;
            }

            temp /= 10;
        }

        num1 * num2
    }
}
