// https://adventofcode.com/2016/day/3

use std::fs;

fn part2(input: &str) -> u32 {
    let mut valid_triangles: u32 = 0;
    let rows: Vec<Vec<u32>> = input
        .lines()
        .map(|line| {
            line.split_whitespace()
                .map(|num| num.parse().unwrap())
                .collect()
        })
        .collect();

    fn is_valid(mut sides: [u32; 3]) -> bool {
        if sides[0] > sides[1] {
            sides.swap(0, 1);
        }
        if sides[1] > sides[2] {
            sides.swap(1, 2);
        }
        if sides[0] > sides[1] {
            sides.swap(0, 1);
        }

        sides[0] + sides[1] > sides[2]
    }

    for chunk in rows.chunks(3) {
        let triangle_1: [u32; 3] = [chunk[0][0], chunk[1][0], chunk[2][0]];
        let triangle_2: [u32; 3] = [chunk[0][1], chunk[1][1], chunk[2][1]];
        let triangle_3: [u32; 3] = [chunk[0][2], chunk[1][2], chunk[2][2]];

        if is_valid(triangle_1) {
            valid_triangles += 1;
        }
        if is_valid(triangle_2) {
            valid_triangles += 1;
        }
        if is_valid(triangle_3) {
            valid_triangles += 1;
        }
    }

    valid_triangles
}

fn main() {
    let input = fs::read_to_string("input.txt").expect("Failed to read input file");

    println!("Part 2: {}", part2(&input));
}
