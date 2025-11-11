// https://adventofcode.com/2015/day/5

use std::collections::HashSet;
use std::fs;

fn part1(input: &str) -> u32 {
    let mut nice_count: u32 = 0;
    let vowels: HashSet<char> = HashSet::from(['a', 'e', 'i', 'o', 'u']);
    let forbidden: HashSet<&str> = HashSet::from(["ab", "cd", "pq", "xy"]);

    for line in input.lines() {
        let mut vowel_count: u32 = 0;
        let mut has_double: bool = false;
        let mut is_valid: bool = true;

        let mut prev_char: char = '\0';
        for current_char in line.chars() {
            let pair: String = format!("{}{}", prev_char, current_char);

            if vowels.contains(&current_char) {
                vowel_count += 1;
            }
            if current_char == prev_char {
                has_double = true;
            }
            if forbidden.contains(pair.as_str()) {
                is_valid = false
            }
            prev_char = current_char;
        }
        if vowel_count >= 3 && has_double && is_valid {
            nice_count += 1;
        }
    }

    nice_count
}

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

    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}

