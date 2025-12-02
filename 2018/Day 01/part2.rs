// https://adventofcode.com/2018/day/1

use std::{collections::HashSet, fs};

fn part2(input: &str) -> i32 {
    let mut frequency: i32 = 0;
    let mut frequency_set: HashSet<i32> = HashSet::new();
    frequency_set.insert(0);

    loop {
        for line in input.lines() {
            let number: i32 = line.parse().expect("Invalid number");
            frequency += number;

            if frequency_set.contains(&frequency) {
                return frequency;
            }
            frequency_set.insert(frequency);
        }
    }
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 2: {}", part2(&input));
}
