// https://adventofcode.com/2025/day/7

use std::{
    collections::{HashSet, VecDeque},
    fs,
};

fn part1(input: &str) -> u32 {
    let mut beam_splits: u32 = 0;

    let mut splitters: Vec<(usize, usize)> = Vec::new();
    let mut tachyon_beams: VecDeque<(usize, usize)> = VecDeque::new();
    let mut hashset: HashSet<(usize, usize)> = HashSet::new();

    for (row, line) in input.lines().enumerate() {
        for (col, chr) in line.chars().enumerate() {
            match chr {
                'S' => tachyon_beams.push_back((row, col)),
                '^' => splitters.push((row, col)),
                _ => {}
            }
        }
    }

    while tachyon_beams.len() > 0 {
        let beam = tachyon_beams.pop_front().unwrap();

        if hashset.contains(&beam) {
            continue;
        } else {
            hashset.insert(beam);
            beam_splits += 1;
        }

        for splitter in &splitters {
            if splitter.1 == beam.1 && splitter.0 > beam.0 {
                tachyon_beams.push_back((splitter.0, splitter.1 - 1));
                tachyon_beams.push_back((splitter.0, splitter.1 + 1));
            }
        }
    }

    beam_splits
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
}
