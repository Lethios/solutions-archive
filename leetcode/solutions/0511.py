# https://leetcode.com/problems/game-play-analysis-i/

import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity.sort_values(by="event_date", inplace=True)
    activity.drop_duplicates(subset="player_id", keep="first", inplace=True)
    return activity[["player_id", "event_date"]].rename(columns={"event_date": "first_login"})
