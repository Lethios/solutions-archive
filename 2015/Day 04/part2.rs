// https://adventofcode.com/2015/day/4

use md5::{Digest, Md5};

fn part2(input: &str) -> u32 {
    let mut number: u32 = 0;

    let key: u32 = loop {
        let mut hasher = Md5::new();

        let payload: String = format!("{input}{number}");
        hasher.update(payload.as_bytes());

        let hash = hasher.finalize();
        let hash_string: String = format!("{:x}", hash);

        if &hash_string[..6] == "000000" {
            break number;
        }
        number += 1;
    };

    key
}

fn main() {
    let input: String = String::from("<INPUT>");

    println!("Part 2: {}", part2(&input));
}
