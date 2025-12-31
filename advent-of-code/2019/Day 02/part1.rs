// https://adventofcode.com/2019/day/2

use std::fs;

fn part1(input: &str) -> u32 {
    let mut intcode: Vec<u32> = input.trim().split(",").map(|val| val.parse().unwrap()).collect();

    intcode[1] = 12;
    intcode[2] = 2;

    for idx in (0..intcode.len()).step_by(4) {
        match intcode[idx] {
            1 => {
                let a_idx: usize = intcode[idx + 1] as usize;
                let b_idx: usize = intcode[idx + 2] as usize;
                let output_idx: usize = intcode[idx + 3] as usize;

                intcode[output_idx] = intcode[a_idx] + intcode[b_idx];
            },
            2 => {
                let a_idx: usize = intcode[idx + 1] as usize;
                let b_idx: usize = intcode[idx + 2] as usize;
                let output_idx: usize = intcode[idx + 3] as usize;

                intcode[output_idx] = intcode[a_idx] * intcode[b_idx];
            },
            99 => break,
            _ => {}
        }
    }
    
    intcode[0]
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
}
