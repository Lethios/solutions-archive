use core::cmp;
use std::io::{self, BufRead};

fn part1() -> u32 {
    let stdin = io::stdin();
    let mut total_sum: u32 = 0;

    for line in stdin.lock().lines() {
        let expr: String = line.expect("Failed to read line");

        let dimensions: Vec<u32> = expr
            .split("x")
            .map(|dim| dim.parse().expect("Failed to parse number"))
            .collect();

        let (l, w, h) = (dimensions[0], dimensions[1], dimensions[2]);
        let sur_area = (2 * l * w) + (2 * w * h) + (2 * h * l);
        total_sum += sur_area + cmp::min(l * w, cmp::min(w * h, h * l));
    }

    total_sum
}

fn main() {
    println!("Part 1: {}", part1())
}

