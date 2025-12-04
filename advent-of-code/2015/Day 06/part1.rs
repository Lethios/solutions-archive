// https://adventofcode.com/2015/day/6

use std::fs;

fn part1(input: &str) -> u32 {
    let mut light_grid: Vec<[bool; 1000]> = vec![[false; 1000]; 1000];

    for line in input.lines() {
        let args: Vec<&str> = line.split_whitespace().collect();

        let start_coords: Vec<usize> = args[if args[0] == "turn" { 2 } else { 1 }]
            .split(",")
            .map(|num| num.parse().unwrap())
            .collect();
        let end_coords: Vec<usize> = args[args.len() - 1]
            .split(",")
            .map(|num| num.parse().unwrap())
            .collect();

        match args[0] {
            "turn" => match args[1] {
                "on" => {
                    for row in start_coords[0]..=end_coords[0] {
                        for col in start_coords[1]..=end_coords[1] {
                            light_grid[row][col] = true;
                        }
                    }
                }
                "off" => {
                    for row in start_coords[0]..=end_coords[0] {
                        for col in start_coords[1]..=end_coords[1] {
                            light_grid[row][col] = false;
                        }
                    }
                }
                _ => {}
            },
            "toggle" => {
                for row in start_coords[0]..=end_coords[0] {
                    for col in start_coords[1]..=end_coords[1] {
                        light_grid[row][col] = !light_grid[row][col];
                    }
                }
            }
            _ => {}
        }
    }

    let mut lit_count: u32 = 0;
    for row in 0..1000 {
        for col in 0..1000 {
            lit_count = if light_grid[row][col] {
                lit_count + 1
            } else {
                lit_count
            };
        }
    }

    lit_count
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
}
