// https://adventofcode.com/2016/day/2

use std::fs;

fn part1(input: &str) -> String {
    let mut ans = String::with_capacity(input.lines().count());

    let keypad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']];

    let mut row: usize = 1;
    let mut col: usize = 1;

    for line in input.lines() {
        for direction in line.chars() {
            match direction {
                'U' => row = row.saturating_sub(1),
                'D' => row = (row + 1).min(2),
                'L' => col = col.saturating_sub(1),
                'R' => col = (col + 1).min(2),
                _ => {}
            }
        }
        ans.push(keypad[row][col]);
    }

    ans
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
}
