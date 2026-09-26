// https://adventofcode.com/2025/day/7

use std::fs;

fn part2(input: &str) -> u64 {
    let mut loc = [0_u64; 142];

    for line in input.lines() {
        for (i, char) in line.chars().enumerate() {
            if char == 'S' {
                loc[i] = 1;
            } else if char == '^' && loc[i] > 0 {
                if i > 0 {
                    loc[i - 1] += loc[i];
                }

                if i + 1 < loc.len() {
                    loc[i + 1] += loc[i];
                }

                loc[i] = 0;
            }
        }
    }

    loc.iter().sum()
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 2: {}", part2(&input));
}
