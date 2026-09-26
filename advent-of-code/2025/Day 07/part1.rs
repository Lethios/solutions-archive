// https://adventofcode.com/2025/day/7

use std::fs;

fn part1(input: &str) -> i32 {
    let mut loc = [false; 142];
    let mut res = 0;

    for line in input.lines() {
        for (i, char) in line.chars().enumerate() {
            if char == 'S' {
                loc[i] = true;
            } else if char == '^' && loc[i] {
                loc[i] = false;

                if i > 0 {
                    loc[i - 1] = true;
                }

                if i + 1 < loc.len() {
                    loc[i + 1] = true;
                }

                res += 1;
            }
        }
    }

    res
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
}
