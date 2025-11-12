// https://adventofcode.com/2021/day/1

use std::fs;

fn part1(input: &str) -> u32 {
    let mut increase_count: u32 = 0;
    let mut prev_depth: u32 = 10000;

    for line in input.lines() {
        let depth: u32 = line.parse().expect("Invalid number");
        if depth > prev_depth {
            increase_count += 1;
        }
        prev_depth = depth;
    }

    increase_count
}

fn part2(input: &str) -> u32 {
    let mut increase_count: u32 = 0;
    let depth_vector: Vec<u32> = input.lines().map(|depth| depth.parse().unwrap()).collect();

    let mut prev_depth_sum: u32 = depth_vector[0] + depth_vector[1] + depth_vector[2];
    for (index, depth) in depth_vector.iter().enumerate().skip(3) {
        let depth_sum: u32 = prev_depth_sum - depth_vector[index - 3] + depth;

        if depth_sum > prev_depth_sum {
            increase_count += 1;
        }
        prev_depth_sum = depth_sum;
    }

    increase_count
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}
