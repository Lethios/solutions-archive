// https://leetcode.com/problems/1-bit-and-2-bit-characters/description/

impl Solution {
    pub fn is_one_bit_character(bits: Vec<i32>) -> bool {
        let len: usize = bits.len();
        let mut i: usize = 0;

        while i < len - 1 {
            i += (bits[i] as usize) + 1; 
        }

        i == len - 1
    }
}
