// https://adventofcode.com/2018/day/1

use std::{collections::HashSet, fs};

fn part1(input: &str) -> i32 {
    let mut frequency: i32 = 0;

    for line in input.lines() {
        let number: i32 = line.parse().expect("Invalid number");
        frequency += number;
    }

    frequency
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
}
