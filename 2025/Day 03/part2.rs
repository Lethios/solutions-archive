// https://adventofcode.com/2025/day/3

use std::fs;

fn part2(input: &str) -> u64 {
    let mut max_joltage: u64 = 0;

    for bank in input.lines() {
        let line_len: usize = bank.len();
        let bank = bank.bytes();
        let digits: u32 = 12;

        let mut joltage: String = String::new();
        let mut prev_index: usize = 0;

        for digit in 0..digits {
            let bank_copy = bank.clone();
            let mut max_battery: u8 = 0;

            let start: usize = prev_index;
            let end: usize = line_len - (digits - digit) as usize + 1;

            for (index, battery) in bank_copy.enumerate().skip(start).take(end - start) {
                if battery > max_battery {
                    max_battery = battery;
                    prev_index = index;
                }
            }
            prev_index += 1;
            joltage = format!("{}{}", joltage, max_battery - b'0');
        }
        max_joltage += joltage.parse::<u64>().unwrap();
    }

    max_joltage
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 2: {}", part2(&input));
}
