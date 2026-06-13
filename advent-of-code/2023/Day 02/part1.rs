// https://adventofcode.com/2023/day/2

use std::fs;

fn part1(input: &str) -> u32 {
    let mut id_sum: u32 = 0;

    for line in input.lines() {
        let (game, rest) = line.split_once(": ").unwrap();

        let id: u32 = game
            .split_whitespace()
            .nth(1)
            .unwrap()
            .parse()
            .unwrap();

        let mut is_valid: bool = true;

        for set in rest.split("; ") {
            for cube in set.split(", ") {
                let mut parts = cube.split_whitespace();

                let count: u32 = parts.next().unwrap().parse().unwrap();
                let color = parts.next().unwrap();

                match color {
                    "red" => if count > 12 { is_valid = false },
                    "green" => if count > 13 { is_valid = false },
                    "blue" => if count > 14 { is_valid = false },
                    _ => unreachable!(),
                }
            }
        }

        if is_valid {
            id_sum += id;
        }
    }

    id_sum
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
}
