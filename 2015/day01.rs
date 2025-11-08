// https://adventofcode.com/2015/day/1

fn part1() {
    let input: &str = "<INPUT>";
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
