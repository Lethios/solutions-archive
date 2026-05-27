// https://projecteuler.net/problem=31

fn coin_sums(val: usize) -> usize {
    let mut dp: Vec<usize> = vec![0; val + 1];
    dp[0] = 1;

    let coins: [usize; 8] = [1, 2, 5, 10, 20, 50, 100, 200];

    for coin in coins {
        for i in coin..=val {
            dp[i as usize] += dp[i as usize - coin as usize];
        }
    }

    dp[val]
}

fn main() {
    println!("Answer: {}", coin_sums(200))
    // 73682
}
