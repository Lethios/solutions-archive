// https://projecteuler.net/problem=25

use num_bigint::BigUint;

fn fibonacci_1000_digit_number() -> i32 {
    let mut term: i32 = 1;

    let mut a: BigUint = BigUint::from(0u32);
    let mut b: BigUint = BigUint::from(1u32);

    loop {
        if b.to_string().len() >= 1000 {
            return term;
        }

        let temp: BigUint = b.clone();

        b += a;
        a = temp;
        term += 1;
    }
}

fn main() {
    println!("Answer: {}", fibonacci_1000_digit_number())
    // 4782
}
