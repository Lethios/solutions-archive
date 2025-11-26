// https://leetcode.com/problems/smallest-integer-divisible-by-k/

impl Solution {
    pub fn smallest_repunit_div_by_k(k: i32) -> i32 {
        if k % 2 == 0 || k % 5 == 0 {
            return -1;
        }

        let mut ans = 1;
        let mut n = 1 % k;

        while n != 0 {
            n = (n * 10 + 1) % k;
            ans += 1;

            if ans > k {
                return -1;
            }
        }

        ans
    }
}
