// https://adventofcode.com/2025/day/4

use std::fs;

fn part2(input: &str) -> u32 {
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

    let mut removed_this_iteration: u32 = 10000;

    while removed_this_iteration > 0 {
        removed_this_iteration = 0;

        for row in 0..grid.len() {
            for col in 0..grid[0].len() {
                if grid[row][col] == '.' {
                    continue;
                }

                let mut neighbor_count = 0;

                for (d_row, d_col) in adjacent_tiles {
                    let x = row as isize + d_row;
                    let y = col as isize + d_col;

                    if x >= 0 && y >= 0 && (x as usize) < grid.len() && (y as usize) < grid[0].len()
                    {
                        if grid[x as usize][y as usize] == '@' {
                            neighbor_count += 1;
                        }
                    }
                }

                if neighbor_count < 4 {
                    accessible_rolls += 1;
                    removed_this_iteration += 1;

                    grid[row][col] = '.';
                }
            }
        }
    }

    accessible_rolls
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 2: {}", part2(&input));
}


