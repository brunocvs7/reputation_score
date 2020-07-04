# Libs
import os
import datetime

import pandas as pd
from src.data_acquisition import get_tweets

# Constants
CURRENT_PATH = os.getcwd()
DATA_OUTPUT_NAME_RAW = ''
DATA_OUTPUT_PATH_RAW = os.path.join(CURRENT_PATH, 'data', 'raw', DATA_OUTPUT_NAME_RAW)
INITIAL_DATE = ''
FINAL_DATE = ''
QUERY = ''

# Data Structures
range_dates = pd.date_range(INITIAL_DATE, FINAL_DATE)
logs_fail = []

# Bring first day of the list
since_first_date = range_dates[0].strftime('%Y-%m-%d')
until_first_date = range_dates[1].strftime('%Y-%m-%d')
try:
    df_tweets = get_tweets(query=QUERY,
                           since=since_first_date, until=until_first_date)
    df_tweets.to_csv(DATA_OUTPUT_PATH, index=False)
except:
    logs_fail.append(since_first_date)

# Loops from 2nd day til the last
for date in range_dates[1:]:
    until = date + datetime.timedelta(days=1)
    until = until.strftime('%Y-%m-%d')
    since = date.strftime('%Y-%m-%d')
    print("-----Start: ", since, "Until: ", until, "-----")
    try:
        df_tweets = get_tweets(query=QUERY, since=since, until=until)
    except:
        logs_fail.append(since)
    else:
        df_tweets.to_csv(DATA_OUTPUT_PATH, index=False, header=False, mode='a')