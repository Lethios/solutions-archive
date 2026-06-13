// https://adventofcode.com/2023/day/1

use std::fs;

fn part2(input: &str) -> u32 {
    let mut calibration_sum: u32 = 0;

    let words: [(&str, u32); 9] = [
    ("one", 1),
    ("two", 2),
    ("three", 3),
    ("four", 4),
    ("five", 5),
    ("six", 6),
    ("seven", 7),
    ("eight", 8),
    ("nine", 9),
];

    for line in input.lines() {
        let mut digits: Vec<u32> = Vec::new();

        for (idx, chr) in line.chars().enumerate() {
            if chr.to_digit(10).is_some() {
                digits.push(chr.to_digit(10).unwrap());
            }

            let check: &str = &line[idx..];

            for (word, num) in words {
                if check.starts_with(word) {
                    digits.push(num);
                    break;
                }
            }

        }

        calibration_sum += digits[0] * 10 + digits.last().unwrap();
    }

    calibration_sum
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 2: {}", part2(&input));
}
