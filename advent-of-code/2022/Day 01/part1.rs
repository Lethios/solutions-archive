// https://adventofcode.com/2022/day/1

use std::{cmp, collections::BinaryHeap, fs};

fn part1(input: &str) -> u32 {
    let mut max_calorie_sum: u32 = 0;
    let mut calorie_sum: u32 = 0;

    for line in input.lines() {
        match line.parse::<u32>() {
            Ok(calories) => calorie_sum += calories,
            Err(_) => {
                max_calorie_sum = cmp::max(max_calorie_sum, calorie_sum);
                calorie_sum = 0;
            }
        };
    }

    cmp::max(max_calorie_sum, calorie_sum)
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
}
