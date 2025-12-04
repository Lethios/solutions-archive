// https://adventofcode.com/2025/day/3

use std::fs;

fn part1(input: &str) -> u32 {
    let mut max_joltage: u32 = 0;

    for bank in input.lines() {
        let mut bank = bank.bytes();
        let last_num: u8 = bank.next_back().unwrap();

        let mut max_val: (usize, u8) = (0, 0);

        for (i, battery) in bank.clone().enumerate() {
            if battery > max_val.1 {
                max_val.0 = i;
                max_val.1 = battery;
            }
        }
        let first_num: u32 = (max_val.1 - b'0') as u32;

        max_val.1 = 0;
        for battery in bank.skip(max_val.0 + 1) {
            if battery > max_val.1 {
                max_val.1 = battery;
            }
        }
        let loop_val = if max_val.1 > 0 { max_val.1 - b'0' } else { 0 };
        let second_num: u32 = loop_val.max(last_num - b'0') as u32;

        max_joltage += first_num * 10 + second_num;
    }

    max_joltage
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
}

