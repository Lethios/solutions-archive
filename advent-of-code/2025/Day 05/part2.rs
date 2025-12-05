// https://adventofcode.com/2025/day/5

use std::fs;

fn part2(input: &str) -> u64 {
    let mut id_ranges: Vec<Vec<u64>> = Vec::new();

    for line in input.lines() {
        if line.trim().is_empty() {
            break;
        }

        let id_range: Vec<u64> = line
            .split("-")
            .map(|range| range.parse().unwrap())
            .collect();

        id_ranges.push(id_range);
    }

    id_ranges.sort_unstable();
    let mut merged_intervals: Vec<(u64, u64)> = Vec::new();

    for range in id_ranges {
        let start: u64 = range[0];
        let end: u64 = range[1];

        if let Some(last) = merged_intervals.last_mut() {
            if start <= last.1 + 1 {
                last.1 = last.1.max(end);
            } else {
                merged_intervals.push((start, end));
            }
        } else {
            merged_intervals.push((start, end));
        }
    }

    let fresh_ingredients: u64 = merged_intervals
        .iter()
        .map(|(start, end)| end - start + 1)
        .sum();

    fresh_ingredients
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 2: {}", part2(&input));
}

