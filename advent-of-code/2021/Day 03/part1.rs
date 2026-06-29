// https://adventofcode.com/2021/day/3

use std::fs;

fn part1(input: &str) -> u32 {
    let mut arr = vec![0i32; input.lines().next().unwrap().len()];

    for line in input.lines() {
        for (idx, bit) in line.bytes().enumerate() {
            let val: i32 = if bit == b'1' { 1 } else { -1 };

            arr[idx] += val;
        }
    }

    let mut gamma: u32 = 0;

    for &val in &arr {
        gamma <<= 1;

        if val > 0 {
            gamma |= 1;
        }
    }

    let mask = (1 << arr.len()) - 1;
    let epsilon: u32 = !gamma & mask;

    gamma * epsilon
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
}
