// https://adventofcode.com/2025/day/6

use std::fs;

fn part1(input: &str) -> u64 {
    let mut rows = input.lines().rev();

    let mut problem_list: Vec<(char, u64)> = rows
        .next()
        .unwrap()
        .split_whitespace()
        .map(|op| {
            let operation = op.chars().next().unwrap();
            let initial_value = if operation == '*' { 1 } else { 0 };
            (operation, initial_value)
        })
        .collect();

    for row in rows {
        let buffer: Vec<u64> = row
            .split_whitespace()
            .map(|num| num.parse().unwrap())
            .collect();

        for (index, num) in buffer.iter().enumerate() {
            match problem_list[index].0 {
                '+' => problem_list[index].1 += num,
                '*' => problem_list[index].1 *= num,
                _ => {}
            }
        }
    }
    let problem_sums = problem_list.iter().map(|tuple| tuple.1).sum();

    problem_sums
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
}


