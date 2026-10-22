# https://leetcode.com/problems/second-highest-salary/

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    res = employee["salary"].drop_duplicates().sort_values(ascending=False)
    return pd.DataFrame({"SecondHighestSalary": [res.iloc[1] if len(res) >= 2 else None]})
