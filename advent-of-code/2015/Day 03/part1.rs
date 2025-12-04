// https://adventofcode.com/2015/day/3

use std::collections::HashSet;
use std::fs;

fn part1(input: &str) -> usize {
    let mut visited: HashSet<(i32, i32)> = HashSet::new();
    visited.insert((0, 0));

    let mut x: i32 = 0;
    let mut y: i32 = 0;

    for chr in input.chars() {
        match chr {
            '<' => x -= 1,
            'v' => y -= 1,
            '^' => y += 1,
            '>' => x += 1,
            _ => {}
        }
        visited.insert((x, y));
    }

    visited.len()
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read file");

    println!("Part 1: {}", part1(&input));
}
