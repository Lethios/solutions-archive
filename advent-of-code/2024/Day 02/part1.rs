// https://adventofcode.com/2024/day/2

use std::fs;

fn part1(input: &str) -> u32 {
    let mut safe_reports: u32 = 0;

    for line in input.lines() {
        let levels: Vec<i32> = line
            .split_whitespace()
            .map(|num| num.parse().unwrap())
            .collect();

        let windows: Vec<i32> = levels.windows(2).map(|w| w[1] - w[0]).collect();

        let all_increasing: bool = windows.iter().all(|&diff| 0 < diff && diff <= 3);
        let all_decreasing: bool = windows.iter().all(|&diff| 0 > diff && diff >= -3);

        if all_increasing || all_decreasing {
            safe_reports += 1;
        }
    }

    safe_reports
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
}
