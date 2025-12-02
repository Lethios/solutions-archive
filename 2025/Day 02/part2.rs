// https://adventofcode.com/2025/day/2

use std::fs;

fn part2(input: &str) -> u64 {
    let mut invalid_id_sum: u64 = 0;

    let id_ranges: Vec<u64> = input
        .trim()
        .split([',', '-'])
        .map(|num| num.parse().unwrap())
        .collect();

    for chunk in id_ranges.chunks(2) {
        for num in chunk[0]..=chunk[1] {
            let str_num: String = num.to_string();

            for pattern_len in 1..=str_num.len() / 2 {
                if str_num.len() % pattern_len != 0 {
                    continue;
                }

                let pattern: &str = &str_num[..pattern_len];
                let pattern_check = pattern.repeat(str_num.len() / pattern_len);

                if pattern_check == str_num {
                    invalid_id_sum += num;
                    break;
                }
            }
        }
    }

    invalid_id_sum
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 2: {}", part2(&input));
}
