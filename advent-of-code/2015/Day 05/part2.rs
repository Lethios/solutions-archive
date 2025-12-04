// https://adventofcode.com/2015/day/5

use std::collections::HashSet;
use std::fs;

fn part2(input: &str) -> u32 {
    let mut nice_count: u32 = 0;

    for line in input.lines() {
        let mut has_pair: bool = false;
        let bytes: &[u8] = line.as_bytes();
        for i in 0..bytes.len() - 1 {
            let pair: &[u8] = &bytes[i..i + 2];

            for j in i + 2..bytes.len() - 1 {
                let next_pair: &[u8] = &bytes[j..j + 2];
                if pair == next_pair {
                    has_pair = true;
                    break;
                }
            }
            if has_pair {
                break;
            }
        }
        let has_repeat: bool = line.as_bytes().windows(3).any(|w| w[0] == w[2]);

        if has_pair && has_repeat {
            nice_count += 1;
        }
    }

    nice_count
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 2: {}", part2(&input));
}
