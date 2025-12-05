// https://adventofcode.com/2025/day/5

use std::fs;

fn part1(input: &str) -> u32 {
    let mut fresh_ingredients: u32 = 0;

    let mut id_ranges: Vec<Vec<u64>> = Vec::new();
    let mut available_ingredients: Vec<u64> = Vec::new();
    let mut available: bool = false;

    for line in input.lines() {
        if line.trim().is_empty() {
            available = true;
            continue;
        }

        if !available {
            let id_range: Vec<u64> = line
                .split("-")
                .map(|range| range.parse().unwrap())
                .collect();

            id_ranges.push(id_range);
        } else {
            available_ingredients.push(line.parse().unwrap());
        }
    }

    for ingredient in available_ingredients {
        for range in &id_ranges {
            if range[0] <= ingredient && ingredient <= range[1] {
                fresh_ingredients += 1;
                break;
            }
        }
    }

    fresh_ingredients
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 1: {}", part1(&input));
}


