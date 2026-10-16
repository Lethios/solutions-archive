# https://leetcode.com/problems/rising-temperature/

import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    res = weather.sort_values(by="recordDate")
    return res[(res["recordDate"].diff().dt.days == 1) & (res["temperature"].diff() > 0)][["id"]]
