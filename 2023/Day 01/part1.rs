// https://adventofcode.com/2023/day/1

use std::fs;

fn part1(input: &str) -> u32 {
    let mut calibration_sum: u32 = 0;

    for line in input.lines() {
        let digits: Vec<u32> = line.chars().filter_map(|chr| chr.to_digit(10)).collect();
        let calibration_value: u32 = format!("{}{}", digits[0], digits.last().unwrap())
            .parse()
            .unwrap();

        calibration_sum += calibration_value;
    }

    calibration_sum
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
}


