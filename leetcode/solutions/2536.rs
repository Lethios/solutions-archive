// https://leetcode.com/problems/increment-submatrices-by-one/

impl Solution {
    pub fn range_add_queries(n: i32, queries: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let n: usize = n as usize;
        let mut mat: Vec<Vec<i32>> = vec![vec![0; n + 1]; n + 1];

        for query in queries {
            let [r1, c1, r2, c2] = query.try_into().unwrap();
            let (r1, c1, r2, c2) = (r1 as usize, c1 as usize, r2 as usize, c2 as usize);

            mat[r1][c1] += 1;
            mat[r2 + 1][c1] -= 1;
            mat[r1][c2 + 1] -= 1;
            mat[r2 + 1][c2 + 1] += 1;
        }

        for row in 1..=n {
            for col in 0..=n {
                mat[row][col] += mat[row - 1][col];
            }
        }

        for row in 0..=n {
            for col in 1..=n {
                mat[row][col] += mat[row][col - 1];
            }
        }

        let mat: Vec<Vec<i32>> = mat[..n]
            .iter()
            .map(|row| row[..n].to_vec())
            .collect();

        mat
    }
}

