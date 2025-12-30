// https://adventofcode.com/2018/day/2

use std::{collections::HashMap, fs};

fn part1(input: &str) -> u32 {
    let mut two_id: u32 = 0;
    let mut three_id: u32 = 0;

    for line in input.lines() {
        let mut counts: HashMap<char, u32> = HashMap::new();

        for chr in line.chars() {
            *counts.entry(chr).or_insert(0) += 1;
        }

        let two_present: bool = counts.values().any(|&val| val == 2);
        let three_present: bool = counts.values().any(|&val| val == 3);

        if two_present {
            two_id += 1;
        }
        if three_present {
            three_id += 1;
        }
    }

    two_id * three_id
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
}
