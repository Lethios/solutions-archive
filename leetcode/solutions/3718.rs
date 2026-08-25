// https://leetcode.com/problems/smallest-missing-multiple-of-k/

impl Solution {
    pub fn missing_multiple(nums: Vec<i32>, k: i32) -> i32 {
        let mut set = std::collections::HashSet::new();

        for num in nums {
            if num % k == 0 {
                set.insert(num);
            }
        }

        let mut i = 0;
        loop {
            i += 1;

            if set.contains(&(k * i)) {
                continue;
            }

            return k * i;
        }
    }
}
