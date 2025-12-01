// https://adventofcode.com/2025/day/1

use std::fs;

fn part1(input: &str) -> u32 {
    let mut zero_pointing: u32 = 0;
    let mut dial: i32 = 50;

    for line in input.lines() {
        let distance: i32 = line[1..line.len()]
            .parse()
            .expect("Failed to parse integer");

        match line.as_bytes().get(0) {
            Some(b'L') => {
                dial = (dial - distance) % 100;
            }
            Some(b'R') => {
                dial = (dial + distance) % 100;
            }
            _ => {}
        }

        if dial == 0 {
            zero_pointing += 1;
        }
    }

    zero_pointing
}

fn part2(input: &str) -> u32 {
    let mut zero_pointing: u32 = 0;
    let mut dial: i32 = 50;

    for line in input.lines() {
        let distance: i32 = line[1..line.len()]
            .parse()
            .expect("Failed to parse integer");

        match line.as_bytes().get(0) {
            Some(b'L') => {
                let new_position: i32 = dial - distance;

                if new_position < 0 {
                    zero_pointing += (-new_position / 100 + 1) as u32;
                }
                dial = (new_position) % 100;
            }
            Some(b'R') => {
                let new_position: i32 = dial + distance;

                if new_position > 99 {
                    zero_pointing += (new_position / 100) as u32;
                }
                dial = (new_position) % 100;
            }
            _ => {}
        }

        if dial == 0 {
            zero_pointing += 1;
        }
    }

    zero_pointing
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}

