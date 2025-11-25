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

fn part2(input: &str) -> String {
    let mut ans = String::with_capacity(input.lines().count());

    let keypad = [
        ['0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '1', '0', '0', '0'],
        ['0', '0', '2', '3', '4', '0', '0'],
        ['0', '5', '6', '7', '8', '9', '0'],
        ['0', '0', 'A', 'B', 'C', '0', '0'],
        ['0', '0', '0', 'D', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0'],
    ];

    let mut row: usize = 3;
    let mut col: usize = 1;

    for line in input.lines() {
        for direction in line.chars() {
            match direction {
                'U' => {
                    if keypad[row - 1][col] != '0' {
                        row -= 1
                    }
                }
                'D' => {
                    if keypad[row + 1][col] != '0' {
                        row += 1
                    }
                }
                'L' => {
                    if keypad[row][col - 1] != '0' {
                        col -= 1
                    }
                }
                'R' => {
                    if keypad[row][col + 1] != '0' {
                        col += 1
                    }
                }
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
    println!("Part 2: {}", part2(&input));
}

