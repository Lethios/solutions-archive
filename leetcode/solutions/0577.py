# https://leetcode.com/problems/employee-bonus/

import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    res = pd.merge(employee, bonus, on="empId", how="left")[["name", "bonus"]]
    return res[(res.bonus < 1000) | (res.bonus.isna())]
