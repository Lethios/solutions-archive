// https://adventofcode.com/2017/day/1

fn part2(input: &str) -> u32 {
    let len: usize = input.len();
    let mut sum: u32 = 0;

    for (i, chr) in input.chars().enumerate() {
        let digit: u32 = chr.to_digit(10).unwrap();
        let index: usize = (i + (len / 2)) % len;

        let half = input.chars().nth(index).unwrap().to_digit(10).unwrap();

        if digit == half {
            sum += digit;
        }
    }

    sum
}

fn main() {
    let input: &str = "<INPUT>";

    println!("Part 2: {}", part2(input));
}
