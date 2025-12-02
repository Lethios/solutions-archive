// https://adventofcode.com/2017/day/1

fn part1(input: &str) -> u32 {
    let mut prev: u32 = input.chars().last().unwrap().to_digit(10).unwrap();
    let mut sum: u32 = 0;

    for chr in input.chars() {
        let digit: u32 = chr.to_digit(10).unwrap();

        if digit == prev {
            sum += digit;
        }
        prev = digit;
    }

    sum
}

fn main() {
    let input: &str = "<INPUT>";

    println!("Part 1: {}", part1(input));
}
