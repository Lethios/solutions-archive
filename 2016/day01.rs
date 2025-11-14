// https://adventofcode.com/2016/day/1

use std::{collections::HashSet, fs};

fn part1(input: &str) -> i32 {
    enum Direction {
        North,
        East,
        South,
        West,
    }

    impl Direction {
        fn turn_right(&self) -> Direction {
            match self {
                Direction::North => Direction::East,
                Direction::East => Direction::South,
                Direction::South => Direction::West,
                Direction::West => Direction::North,
            }
        }
        fn turn_left(&self) -> Direction {
            match self {
                Direction::North => Direction::West,
                Direction::West => Direction::South,
                Direction::South => Direction::East,
                Direction::East => Direction::North,
            }
        }
    }

    let commands: Vec<&str> = input.trim().split(", ").collect();
    let mut facing_dir: Direction = Direction::North;

    let mut x: i32 = 0;
    let mut y: i32 = 0;

    for command in commands {
        let direction: char = command.chars().nth(0).unwrap();
        let distance: i32 = command[1..].parse().unwrap();

        facing_dir = match direction {
            'R' => facing_dir.turn_right(),
            'L' => facing_dir.turn_left(),
            _ => facing_dir,
        };

        match facing_dir {
            Direction::North => y += distance,
            Direction::South => y -= distance,
            Direction::East => x += distance,
            Direction::West => x -= distance,
        }
    }

    x.abs() + y.abs()
}

fn part2(input: &str) -> i32 {
    enum Direction {
        North,
        East,
        South,
        West,
    }

    impl Direction {
        fn turn_right(&self) -> Direction {
            match self {
                Direction::North => Direction::East,
                Direction::East => Direction::South,
                Direction::South => Direction::West,
                Direction::West => Direction::North,
            }
        }
        fn turn_left(&self) -> Direction {
            match self {
                Direction::North => Direction::West,
                Direction::West => Direction::South,
                Direction::South => Direction::East,
                Direction::East => Direction::North,
            }
        }
    }

    let commands: Vec<&str> = input.trim().split(", ").collect();
    let mut facing_dir: Direction = Direction::North;

    let mut x: i32 = 0;
    let mut y: i32 = 0;

    let mut visited: HashSet<(i32, i32)> = HashSet::new();
    visited.insert((0, 0));

    for command in commands {
        let direction: char = command.chars().nth(0).unwrap();
        let distance: i32 = command[1..].parse().unwrap();

        facing_dir = match direction {
            'R' => facing_dir.turn_right(),
            'L' => facing_dir.turn_left(),
            _ => facing_dir,
        };

        for _ in 0..distance {
            match facing_dir {
                Direction::North => y += 1,
                Direction::South => y -= 1,
                Direction::East => x += 1,
                Direction::West => x -= 1,
            }

            if visited.contains(&(x, y)) {
                return x.abs() + y.abs();
            }
            visited.insert((x, y));
        }
    }

    x.abs() + y.abs()
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
    println!("Part 2: {}", part2(&input));
}


