// https://projecteuler.net/problem=18

use std::{cmp, fs};

fn maximum_path_sum_i(input: &str) -> u32 {
    let mut triangle: Vec<Vec<u32>> = input
        .lines()
        .map(|line| {
            line.split_whitespace()
                .map(|num| num.parse::<u32>().unwrap())
                .collect()
        })
        .collect();

    for row in (0..triangle.len() - 1).rev() {
        for col in 0..triangle[row].len() {
            triangle[row][col] += cmp::max(triangle[row + 1][col], triangle[row + 1][col + 1]);
        }
    }

    triangle[0][0]
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Answer: {}", maximum_path_sum_i(&input));
    // 1074
}

