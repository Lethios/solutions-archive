// https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

impl Solution {
    pub fn find_the_prefix_common_array(a: Vec<i32>, b: Vec<i32>) -> Vec<i32> {
        let mut seen: u64 = 0;
        let mut res: Vec<i32> = Vec::new();
        let mut temp: i32 = 0;

        for i in 0..a.len() {
            if a[i] == b[i] {
                temp += 1;
                res.push(temp);
                continue;
            }

            if seen & (1 << a[i]) != 0 {
                temp += 1;
            } else {
                seen |= (1 << a[i]);
            }

            if seen & (1 << b[i]) != 0 {
                temp += 1;
            } else {
                seen |= (1 << b[i]);
            }

            res.push(temp);
        }

        res
    }
}
