# https://leetcode.com/problems/customers-who-never-order/

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    res = pd.merge(customers, orders, how="left", left_on="id", right_on="customerId")
    return res[res["customerId"].isna()][["name"]].rename(columns={"name": "Customers"})
