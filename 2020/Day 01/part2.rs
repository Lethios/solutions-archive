// https://adventofcode.com/2020/day/1

use std::{collections::HashSet, fs};

fn part2(input: &str) -> u32 {
    let numbers: Vec<u32> = input.lines().filter_map(|line| line.parse().ok()).collect();

    for i in 0..numbers.len() {
        let anchor: u32 = numbers[i];
        let target: u32 = 2020 - anchor;

        let mut difference_set: HashSet<u32> = HashSet::new();

        for j in i + 1..numbers.len() {
            let difference: u32 = target.saturating_sub(numbers[j]);
            if difference_set.contains(&difference) {
                return Some(anchor * numbers[j] * difference).expect("Error");
            }
            difference_set.insert(numbers[j]);
        }
    }

    0
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 2: {}", part2(&input));
}
