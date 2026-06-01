# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/

impl Solution {
    pub fn minimum_cost(cost: Vec<i32>) -> i32 {
        let mut min_cost: i32 = 0;

        let max_cost: i32 = *cost.iter().max().unwrap();
        let mut freq_arr: Vec<i32> = vec![0; (max_cost + 1) as usize];

        for num in cost {
            freq_arr[num as usize] += 1;
        }

        let mut count = 1;

        for c_cost in (1..freq_arr.len()).rev() {
            while freq_arr[c_cost] > 0 {
                freq_arr[c_cost] -= 1;
                
                if count % 3 == 0 {
                    count += 1;
                    continue;
                }

                min_cost += c_cost as i32;
                count += 1;
            }
        }

        min_cost
    }
}
