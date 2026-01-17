// https://adventofcode.com/2020/day/3

use std::{collections::HashSet, fs};

fn part1(input: &str) -> u32 {
    let mut trees_encountered: u32 = 0;
    let slope: (u32, u32) = (1, 3);

    let lines: Vec<&str> = input.lines().collect();
    let row_len: u32 = lines.len() as u32;
    let col_len: u32 = lines[0].len() as u32;

    let mut tree_set: HashSet<(u32, u32)> = HashSet::new();

    for (row, line) in input.lines().enumerate() {
        for (col, chr) in line.chars().enumerate() {
            if chr == '#' {
                tree_set.insert((row as u32, col as u32));
            }
        }
    }

    let mut current: (u32, u32) = (0, 0);
    for _ in 1..=row_len {
        current = (current.0 + slope.0, (current.1 + slope.1) % col_len);

        if tree_set.contains(&current) {
            trees_encountered += 1;
        }
    }

    trees_encountered
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
}
