// https://adventofcode.com/2024/day/1

use std::{collections::HashMap, fs, iter::zip};

fn part1(input: &str) -> u32 {
    let mut ans: u32 = 0;

    let mut left_list: Vec<u32> = Vec::new();
    let mut right_list: Vec<u32> = Vec::new();

    for line in input.lines() {
        let nums: Vec<u32> = line
            .split_whitespace()
            .map(|line| line.parse().unwrap())
            .collect();

        left_list.push(nums[0]);
        right_list.push(nums[1]);
    }
    left_list.sort_unstable();
    right_list.sort_unstable();

    for (left_num, right_num) in zip(left_list, right_list) {
        ans += left_num.abs_diff(right_num);
    }

    ans
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
}
