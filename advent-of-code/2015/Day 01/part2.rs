// https://adventofcode.com/2015/day/1

use std::fs;

fn part2(input: &str) -> usize {
    let mut floor: i32 = 0;

    for (index, chr) in input.chars().enumerate() {
        match chr {
            '(' => floor += 1,
            ')' => floor -= 1,
            _ => {}
        }

        if floor == -1 {
            return index + 1;
        }
    }

    0
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read string");

    println!("Part 2: {}", part2(&input));
}
