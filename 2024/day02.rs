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

fn part2(input: &str) -> u32 {
    let mut safe_reports = 0;

    fn is_safe_report(levels: &[i32]) -> bool {
        let diffs: Vec<_> = levels.windows(2).map(|w| w[1] - w[0]).collect();

        let all_increasing = diffs.iter().all(|&diff| diff >= 1 && diff <= 3);
        let all_decreasing = diffs.iter().all(|&diff| diff <= -1 && diff >= -3);

        all_increasing || all_decreasing
    }

    for line in input.lines() {
        let levels: Vec<i32> = line
            .split_whitespace()
            .map(|num| num.parse().unwrap())
            .collect();

        if is_safe_report(&levels) {
            safe_reports += 1;
            continue;
        }

        let mut found_safe_variant = false;
        for i in 0..levels.len() {
            let mut temp = levels.clone();
            temp.remove(i);

            if is_safe_report(&temp) {
                found_safe_variant = true;
                break;
            }
        }

        if found_safe_variant {
            safe_reports += 1;
        }
    }

    safe_reports
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}

