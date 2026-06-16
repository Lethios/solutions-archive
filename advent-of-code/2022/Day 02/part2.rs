// https://adventofcode.com/2022/day/2

use std::{collections::HashMap, fs};

fn part2(input: &str) -> u32 {
    let mut score: u32 = 0;

    let guide: HashMap<char, (char, u32)> = HashMap::from([
        ('A', ('C', 1)),
        ('B', ('A', 2)),
        ('C', ('B', 3)),
    ]);

    for line in input.lines() {
        let line: Vec<char> = line.chars().collect();

        let choice: char = line[0];
        let outcome: char = line[2];

        match outcome {
            'X' => score += guide[&guide[&choice].0].1,
            'Y' => score += 3 + guide[&choice].1,
            'Z' => score += 6 + guide[&guide[&guide[&choice].0].0].1,
            _ => unreachable!()
        }
    }

    score
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 2: {}", part2(&input));
}
