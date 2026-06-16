// https://adventofcode.com/2022/day/3

use std::{collections::HashSet, fs};

fn part1(input: &str) -> u32 {
    let mut priority_sum: u32 = 0;

    for line in input.lines() {
        let mid: usize = line.len() / 2;

        let left: HashSet<char> = line[..mid].chars().collect();
        let right: HashSet<char> = line[mid..].chars().collect();

        let common: u32 = *left.intersection(&right).next().unwrap() as u32;

        if common >= 'a' as u32 {
            priority_sum += common - 'a' as u32 + 1;
        } else {
            priority_sum += common - 'A' as u32 + 27;
        }
    }

    priority_sum
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
}
