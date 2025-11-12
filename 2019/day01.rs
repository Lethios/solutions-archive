// https://adventofcode.com/2019/day/1

use std::fs;

fn part1(input: &str) -> u32 {
    let mut sum: u32 = 0;

    for line in input.lines() {
        let mass: u32 = line.parse().expect("Invalid number");
        let fuel: u32 = (mass / 3) - 2;
        sum += fuel;
    }

    sum
}

fn part2(input: &str) -> u32 {
    let mut sum: u32 = 0;

    for line in input.lines() {
        let mass: u32 = line.parse().expect("Invalid number");

        let mut fuel: u32 = mass;
        loop {
            fuel = (fuel / 3).saturating_sub(2);
            if fuel == 0 {
                break;
            }
            sum += fuel;
        }
    }

    sum
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}


