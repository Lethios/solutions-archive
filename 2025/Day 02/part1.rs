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
        let start: u64 = chunk[0];
        let end: u64 = chunk[1];

        for num in start..=end {
            let num_len = |mut num: u64| -> u64 {
                let mut count = 0;

                while num > 0 {
                    num /= 10;
                    count += 1;
                }
                count
            };
            let num_len: u64 = num_len(num);

            if num_len % 2 == 1 {
                continue;
            }

            let half: u32 = (num_len / 2) as u32;
            if num / 10u64.pow(half) == num % 10u64.pow(half) {
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
