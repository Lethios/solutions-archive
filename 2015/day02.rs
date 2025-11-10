// https://adventofcode.com/2015/day/2

use core::cmp;
use std::fs;

fn part1(input: &str) -> u32 {
    let mut total_sum: u32 = 0;

    for line in input.lines() {
        let dimensions: Vec<u32> = line
            .split('x')
            .map(|dim| dim.parse().expect("Failed to parse number"))
            .collect();

        let (l, w, h) = (dimensions[0], dimensions[1], dimensions[2]);

        let sur_area = (2 * l * w) + (2 * w * h) + (2 * h * l);
        total_sum += sur_area + cmp::min(l * w, cmp::min(w * h, h * l));
    }

    total_sum
}

fn part2(input: &str) -> u32 {
    let mut total_sum: u32 = 0;

    for line in input.lines() {
        let dimensions: Vec<u32> = line
            .split('x')
            .map(|dim| dim.parse().expect("Failed to parse number"))
            .collect();

        let (l, w, h) = (dimensions[0], dimensions[1], dimensions[2]);

        let perimeter: u32 = 2 * cmp::min(l + w, cmp::min(w + h, h + l));
        let volume: u32 = l * w * h;
        total_sum += perimeter + volume;
    }

    total_sum
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}

