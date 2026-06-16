// https://leetcode.com/problems/process-string-with-special-operations-i/

impl Solution {
    pub fn process_str(s: String) -> String {
        let mut res = String::new();

        for chr in s.chars() {
            match chr {
                '*' => {
                    res.pop();
                }
                '#' => {
                    res.extend_from_within(0..);
                }
                '%' => {
                    res = res.chars().rev().collect();
                }
                _ => {
                    res.push(chr);
                }
            }
        }

        res
    }
}
