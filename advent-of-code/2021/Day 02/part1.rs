// https://adventofcode.com/2021/day/2

use std::fs;

fn part1(input: &str) -> i32 {
    let mut position: i32 = 0;
    let mut depth: i32 = 0;

    for line in input.lines() {
        let mut parts = line.split_whitespace();

        let instruction: &str = parts.next().unwrap();
        let units: i32 = parts.next().unwrap().parse().unwrap();

        match instruction {
            "forward" => position += units,
            "up" => depth -= units,
            "down" => depth += units,
            _ => unreachable!()
        }
    }

    position * depth
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
}
