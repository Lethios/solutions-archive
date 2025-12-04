// https://adventofcode.com/2025/day/4

use std::fs;

fn part1(input: &str) -> u32 {
    let mut accessible_rolls: u32 = 0;

    let mut grid: Vec<Vec<char>> = Vec::with_capacity(input.lines().count());

    for line in input.lines() {
        let row: Vec<char> = line.chars().collect();
        grid.push(row);
    }

    let rows: usize = grid.len();
    let cols: usize = grid[0].len();

    const ADJACENT_TILES: [(isize, isize); 8] = [
        (-1, 1),
        (0, 1),
        (1, 1),
        (-1, 0),
        (1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
    ];

    for row in 0..rows {
        for col in 0..cols {
            if grid[row][col] == '.' {
                continue;
            }

            let mut neighbor_count = 0;

            for (dx, dy) in ADJACENT_TILES {
                let x = row as isize + dx;
                let y = col as isize + dy;

                if x >= 0 && y >= 0 && (x as usize) < rows && (y as usize) < cols {
                    if grid[x as usize][y as usize] == '@' {
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

