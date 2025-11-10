// https://adventofcode.com/2015/day/3

use std::collections::HashSet;
use std::fs;

fn part1(input: &str) -> usize {
    let mut visited: HashSet<(i32, i32)> = HashSet::new();
    visited.insert((0, 0));

    let mut x: i32 = 0;
    let mut y: i32 = 0;

    for chr in input.chars() {
        match chr {
            '<' => x -= 1,
            'v' => y -= 1,
            '^' => y += 1,
            '>' => x += 1,
            _ => {}
        }
        visited.insert((x, y));
    }

    visited.len()
}

fn part2(input: &str) -> usize {
    let mut visited: HashSet<(i32, i32)> = HashSet::new();
    visited.insert((0, 0));

    let mut santa_x: i32 = 0;
    let mut santa_y: i32 = 0;
    let mut robo_x: i32 = 0;
    let mut robo_y: i32 = 0;

    for (index, chr) in input.chars().enumerate() {
        let (x, y): (&mut i32, &mut i32) = if index % 2 == 0 {
            (&mut santa_x, &mut santa_y)
        } else {
            (&mut robo_x, &mut robo_y)
        };

        match chr {
            '<' => *x -= 1,
            'v' => *y -= 1,
            '^' => *y += 1,
            '>' => *x += 1,
            _ => {}
        }
        visited.insert((*x, *y));
    }

    visited.len()
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read file");

    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}
