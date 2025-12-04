// https://adventofcode.com/2022/day/1

use std::{cmp, collections::BinaryHeap, fs};

fn part2(input: &str) -> u32 {
    let mut heap: BinaryHeap<u32> = BinaryHeap::new();
    let mut calorie_sum: u32 = 0;

    for line in input.lines() {
        match line.parse::<u32>() {
            Ok(calories) => calorie_sum += calories,
            Err(_) => {
                heap.push(calorie_sum);
                calorie_sum = 0;
            }
        };
    }
    let max_calories: Vec<_> = (0..3).filter_map(|_| heap.pop()).collect();
    max_calories[0] + max_calories[1] + max_calories[2]
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 2: {}", part2(&input));
}
