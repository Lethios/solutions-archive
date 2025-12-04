// https://adventofcode.com/2024/day/3

use regex::Regex;
use std::fs;

fn part2(input: &str) -> u32 {
    let mut multiplication_sum: u32 = 0;
    let re: Regex = Regex::new(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)").unwrap();

    let mut enabled: bool = true;

    for caps in re.captures_iter(input) {
        match &caps[0] {
            "do()" => enabled = true,
            "don't()" => enabled = false,
            _ => {
                if enabled {
                    multiplication_sum +=
                        caps[1].parse::<u32>().unwrap() * caps[2].parse::<u32>().unwrap();
                }
            }
        }
    }

    multiplication_sum
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 2: {}", part2(&input));
}
