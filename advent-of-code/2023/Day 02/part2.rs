// https://adventofcode.com/2023/day/2

use std::fs;

fn part2(input: &str) -> u32 {
    let mut power_sum: u32 = 0;

    for line in input.lines() {
        let (_, rest) = line.split_once(": ").unwrap();

        let mut min_count: [u32; 3] = [0; 3];

        for set in rest.split("; ") {
            for cube in set.split(", ") {
                let mut parts = cube.split_whitespace();

                let count: u32 = parts.next().unwrap().parse().unwrap();
                let color = parts.next().unwrap();

                match color {
                    "red" => min_count[0] = count.max(min_count[0]),
                    "green" => min_count[1] = count.max(min_count[1]),
                    "blue" => min_count[2] = count.max(min_count[2]),
                    _ => unreachable!(),
                }
            }
        }

        power_sum += min_count[0] * min_count[1] * min_count[2];
    }

    power_sum
}

fn main() {
    let input: String = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 2: {}", part2(&input));
}
