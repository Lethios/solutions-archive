// https://adventofcode.com/2025/day/2

use std::fs;

fn part1(input: &str) -> u64 {
    let mut invalid_id_sum: u64 = 0;

    let id_ranges: Vec<u64> = input
        .trim()
        .split([',', '-'])
        .map(|num| num.parse().unwrap())
        .collect();

    for chunk in id_ranges.chunks(2) {
        for num in chunk[0]..=chunk[1] {
            let str_num: String = num.to_string();

            if str_num.len() % 2 == 1 {
                continue;
            }

            if &str_num[..(str_num.len() / 2)] == (&str_num[(str_num.len() / 2)..]) {
                invalid_id_sum += num;
            }
        }
    }

    invalid_id_sum
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
}
