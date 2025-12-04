// https://adventofcode.com/2025/day/1

use std::fs;

fn part1(input: &str) -> i32 {
    let mut zero_pointing: i32 = 0;
    let mut dial: i32 = 50;

    for line in input.lines() {
        let (direction, distance) = line.split_at(1);
        let distance: i32 = distance.parse().unwrap();

        match direction {
            "L" => {
                dial = (dial - distance).rem_euclid(100);
            }
            "R" => {
                dial = (dial + distance).rem_euclid(100);
            }
            _ => {}
        }

        if dial == 0 {
            zero_pointing += 1;
        }
    }

    zero_pointing
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
}
