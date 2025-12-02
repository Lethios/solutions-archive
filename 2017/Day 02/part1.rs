// https://adventofcode.com/2017/day/2

use std::fs;

fn part1(input: &str) -> u32 {
    let mut checksum: u32 = 0;

    for line in input.lines() {
        let numbers: Vec<u32> = line
            .split_whitespace()
            .filter_map(|num| num.parse().ok())
            .collect();

        let largest: &u32 = numbers.iter().max().unwrap();
        let smallest: &u32 = numbers.iter().min().unwrap();

        checksum += (largest - smallest);
    }

    checksum
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
}
