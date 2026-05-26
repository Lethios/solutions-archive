// https://leetcode.com/problems/count-the-number-of-special-characters-i/

impl Solution {
    pub fn number_of_special_chars(word: String) -> i32 {
        let mut bitmask_lower: u32 = 0;
        let mut bitmask_upper: u32 = 0;

        for chr in word.bytes() {
            if chr.is_ascii_lowercase() {
                bitmask_lower |= (1 << chr - b'a');
            } else {
                bitmask_upper |= (1 << chr - b'A');
            }
        }

        (bitmask_lower & bitmask_upper).count_ones() as i32
    }
}
