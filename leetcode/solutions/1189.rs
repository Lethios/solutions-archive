// https://leetcode.com/problems/maximum-number-of-balloons/

use std::collections::HashMap;

impl Solution {
    pub fn max_number_of_balloons(text: String) -> i32 {
        let mut freq_dict: HashMap<char, i32> = HashMap::from([
            ('b', 0),
            ('a', 0),
            ('l', 0),
            ('o', 0),
            ('n', 0)
        ]);

        for chr in text.chars() {
            *freq_dict.entry(chr).or_insert(0) += 1;
        }

        (((freq_dict[&'b']
            .min(freq_dict[&'a']))
            .min(freq_dict[&'l'] / 2))
            .min(freq_dict[&'o'] / 2))
            .min(freq_dict[&'n'])
    }
}
