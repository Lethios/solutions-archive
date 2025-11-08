// https://adventofcode.com/2015/day/1

fn part1(input: &str) -> i32 {
    let mut floor: i32 = 0;

    for chr in input.chars() {
        match chr {
            '(' => floor += 1,
            ')' => floor -= 1,
            _ => {}
        }
    }

    floor
}

fn part2(input: &str) -> usize {
    let mut floor: i32 = 0;

    for (index, chr) in input.chars().enumerate() {
        match chr {
            '(' => floor += 1,
            ')' => floor -= 1,
            _ => {}
        }

        if floor == -1 {
            return index + 1;
        }
    }

    0
}

fn main() {
    let input: &str = "<INPUT>";

    println!("Part 1: {}", part1(input));
    println!("Part 2: {}", part2(input));
}
