// https://projecteuler.net/problem=112

fn bouncy_numbers(proportion: u32) -> u32 {
    let mut bouncy_count: u32 = 0;
    let mut num: u32 = 100;

    loop {
        let mut increasing = true;
        let mut decreasing = true;

        let mut temp = num;

        let mut prev = temp % 10;
        temp /= 10;

        while temp > 0 {
            let curr = temp % 10;

            if curr < prev {
                increasing = false;
            }

            if curr > prev {
                decreasing = false;
            }

            prev = curr;
            temp /= 10;
        }

        if !increasing && !decreasing {
            bouncy_count += 1;
        }

        if bouncy_count * 100 >= proportion * num {
            return num;
        }

        num += 1;
    }
}

fn main() {
    println!("Answer: {}", bouncy_numbers(99))
    // 1587000
}
