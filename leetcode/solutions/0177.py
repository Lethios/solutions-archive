# https://leetcode.com/problems/nth-highest-salary/

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    res = employee["salary"].drop_duplicates().sort_values(ascending=False)
    return pd.DataFrame({f"getNthHighestSalary({N})": [res.iloc[N - 1] if len(res) >= N and N > 0 else None]})
