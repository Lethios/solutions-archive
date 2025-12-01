// https://adventofcode.com/2025/day/1

use std::fs;

fn part1(input: &str) -> i32 {
    let mut zero_pointing: i32 = 0;
    let mut dial: i32 = 50;

    for line in input.lines() {
        let distance: i32 = line[1..line.len()]
            .parse()
            .expect("Failed to parse integer");

        match line.as_bytes().get(0) {
            Some(b'L') => {
                dial = (dial - distance).rem_euclid(100);
            }
            Some(b'R') => {
                dial = (dial + distance).rem_euclid(100);
            }
            _ => {}
        }

        if dial == 0 {
            zero_pointing += 1;
        }
    }

    zero_pointing
}

fn part2(input: &str) -> i32 {
    let mut zero_pointing: i32 = 0;
    let mut dial: i32 = 50;

    for line in input.lines() {
        let distance: i32 = line[1..line.len()]
            .parse()
            .expect("Failed to parse integer");

        match line.as_bytes().get(0) {
            Some(b'L') => {
                zero_pointing += (100 - dial + distance) / 100 - (100 - dial) / 100;
                dial = (dial - distance).rem_euclid(100);
            }
            Some(b'R') => {
                let new_position: i32 = dial + distance;

                zero_pointing += new_position / 100;
                dial = new_position.rem_euclid(100);
            }
            _ => {}
        }
    }

    zero_pointing
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}

