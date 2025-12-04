// https://adventofcode.com/2016/day/3

use std::fs;

fn part1(input: &str) -> u32 {
    let mut valid_triangles: u32 = 0;

    for line in input.lines() {
        let mut sides: Vec<u32> = line
            .split_whitespace()
            .map(|num| num.parse().unwrap())
            .collect();

        if sides[0] > sides[1] {
            sides.swap(0, 1);
        }
        if sides[1] > sides[2] {
            sides.swap(1, 2);
        }
        if sides[0] > sides[1] {
            sides.swap(0, 1);
        }

        if sides[0] + sides[1] > sides[2] {
            valid_triangles += 1;
        }
    }

    valid_triangles
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
}
