// https://adventofcode.com/2025/day/6

use std::fs;

fn part2(input: &str) -> u64 {
    let lines: Vec<String> = input.lines().map(|s| s.to_string()).collect();
    if lines.is_empty() {
        return 0;
    }

    let max_width = lines.iter().map(|s| s.len()).max().unwrap_or(0);

    let grid: Vec<Vec<char>> = lines
        .iter()
        .map(|line| {
            format!("{:width$}", line, width = max_width)
                .chars()
                .collect()
        })
        .collect();

    let rows = grid.len();
    let op_row_idx = rows - 1;

    let mut grand_total: u64 = 0;

    let mut current_nums: Vec<u64> = Vec::new();
    let mut current_op: Option<char> = None;

    for col in 0..max_width {
        let is_separator = (0..rows).all(|r| grid[r][col] == ' ');

        if is_separator {
            if !current_nums.is_empty() {
                let val = match current_op.unwrap_or('+') {
                    '*' => current_nums.iter().product(),
                    '+' => current_nums.iter().sum(),
                    _ => 0,
                };
                grand_total += val;

                current_nums.clear();
                current_op = None;
            }
        } else {
            let char_at_bottom = grid[op_row_idx][col];
            if char_at_bottom == '+' || char_at_bottom == '*' {
                current_op = Some(char_at_bottom);
            }

            let mut num_str = String::new();
            for r in 0..op_row_idx {
                let c = grid[r][col];
                if c.is_digit(10) {
                    num_str.push(c);
                }
            }

            if !num_str.is_empty() {
                if let Ok(num) = num_str.parse::<u64>() {
                    current_nums.push(num);
                }
            }
        }
    }

    if !current_nums.is_empty() {
        let val = match current_op.unwrap_or('+') {
            '*' => current_nums.iter().product(),
            '+' => current_nums.iter().sum(),
            _ => 0,
        };
        grand_total += val;
    }

    grand_total
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 2: {}", part2(&input));
}


