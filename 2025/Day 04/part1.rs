// https://adventofcode.com/2025/day/4

use std::fs;

fn part1(input: &str) -> u32 {
    let mut accessible_rolls: u32 = 0;
    let mut grid: Vec<Vec<char>> = Vec::new();

    for line in input.lines() {
        let row: Vec<char> = line.chars().collect();
        grid.push(row);
    }

    let adjacent_tiles: [(isize, isize); 8] = [
        (-1, 1),
        (0, 1),
        (1, 1),
        (-1, 0),
        (1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
    ];

    for (x, row) in grid.iter().enumerate() {
        for (y, cell) in row.iter().enumerate() {
            if *cell == '.' {
                continue;
            }

            let mut neighbor_count = 0;

            for (dx, dy) in adjacent_tiles {
                let i = x as isize + dx;
                let j = y as isize + dy;

                if i >= 0 && j >= 0 && (i as usize) < grid.len() && (j as usize) < row.len() {
                    if grid[i as usize][j as usize] == '@' {
                        neighbor_count += 1;
                    }
                }
            }

            if neighbor_count < 4 {
                accessible_rolls += 1;
            }
        }
    }

    accessible_rolls
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
}


