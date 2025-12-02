// https://adventofcode.com/2020/day/1

use std::{collections::HashSet, fs};

fn part1(input: &str) -> u32 {
    let mut difference_set: HashSet<u32> = HashSet::new();
    let mut product: u32 = 0;

    for line in input.lines() {
        let number: u32 = line.parse().expect("Invalid number");
        let difference: u32 = 2020 - number;

        if difference_set.contains(&number) {
            product = number * difference;
        }
        difference_set.insert(difference);
    }

    product
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
}
