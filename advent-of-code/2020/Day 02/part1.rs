// https://adventofcode.com/2020/day/2

use std::fs;

fn part1(input: &str) -> u32 {
    let mut valid_passwords: u32 = 0;

    for line in input.lines() {
        let mut parts = line.split_whitespace();

        let range: Vec<usize> = parts.next().unwrap().split("-").map(|range| range.parse().unwrap()).collect();

        let letter: &str = parts.next().unwrap().strip_suffix(":").unwrap();
        let char_letter: char = letter.chars().nth(0).unwrap();
        let password: &str = parts.next().unwrap();

        let count: usize = password.chars().filter(|&val| val == char_letter).count();

        if range[0] <= count && count <= range[1] {
            valid_passwords += 1;
        }
    }

    valid_passwords
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
}
