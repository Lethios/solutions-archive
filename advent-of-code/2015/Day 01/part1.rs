// https://adventofcode.com/2015/day/1

use std::fs;

fn part1(input: &str) -> i32 {
    let mut floor: i32 = 0;

    for chr in input.chars() {
        match chr {
            '(' => floor += 1,
            ')' => floor -= 1,
            _ => {}
        }
    }

    floor
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read string");

    println!("Part 1: {}", part1(&input));
}
