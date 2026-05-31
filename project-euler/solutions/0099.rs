// https://projecteuler.net/problem=34

use std::fs;

fn digit_factorials(input: String) -> u32 {
    let mut line_num: u32 = 1;
    let mut max: f32 = -1.0;
    let mut max_line_num = 1;

    for line in input.lines() {
        let temp: Vec<&str> = line.split(",").collect();
        let num: f32 = temp[1].parse::<f32>().unwrap() * temp[0].parse::<f32>().unwrap().log10();

        if num > max {
            max = num;
            max_line_num = line_num;
        }

        line_num += 1;
    }

    max_line_num
    
}

fn main() {
    println!("Answer: {}", digit_factorials(fs::read_to_string("input.txt").unwrap()))
    // 709
}
