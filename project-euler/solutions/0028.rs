// https://projecteuler.net/problem=28

fn number_spiral_diagonals(rank: u32) -> u32 {
    let mut sum: u32 = 1;
    let mut curr_rank: u32 = 3;
    let mut num: u32 = 1;

    while curr_rank <= rank {
        for _ in 0..4 {
            let step: u32 = curr_rank - 1;
            
            num += step;
            sum += num;
        }
        
        curr_rank += 2;
    }

    sum
}

fn main() {
    println!("{}", number_spiral_diagonals(1001));
    // 669171001
}
