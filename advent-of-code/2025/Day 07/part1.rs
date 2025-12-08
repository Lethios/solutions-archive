// https://adventofcode.com/2025/day/7

use std::{collections::VecDeque, fs};

fn part1(input: &str) -> u32 {
    let mut beam_splits: u32 = 0;

    let mut splitters: Vec<(usize, usize)> = Vec::new();
    let mut tachyon_beams: VecDeque<(usize, usize)> = VecDeque::new();

    for (row, line) in input.lines().enumerate() {
        for (col, chr) in line.chars().enumerate() {
            match chr {
                'S' => tachyon_beams.push_back((row, col)),
                '^' => splitters.push((row, col)),
                _ => {}
            }
        }
    }
    
    for beam in tachyon_beams {
        for splitter in splitters {
            if splitter.1 == beam.1 && splitter.0 > beam.0 {
                // store beams in hashset to prevent duplicates
            }
        }
    }    
    

    beam_splits
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
}


