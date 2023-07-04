""" Get yahoo finance ticker data and save to file """

from datetime import date, datetime, timedelta

import pandas as pd
import yfinance as yf  # type: ignore
from pandas_datareader import data as pdr  # type: ignore

yf.pdr_override()

# Tickers list
# We can add and delete any ticker from the list to get desired ticker
# live data
ticker_list = ["BURE.ST", "INDU-C.ST", "KINV-B.ST", "LATO-B.ST", "INVE-B.ST"]
today = date.today()

# We can get data by our choice by giving days bracket
START_DATE = datetime.now() - timedelta(days=10)
END_DATE = datetime.now()
files = []


def get_data(ticker):
    """Get yahoo finance ticker data and save to file"""
    print(ticker)
    data = pdr.get_data_yahoo(ticker, start=START_DATE, end=END_DATE)
    dataname = ticker + "_" + str(today)
    files.append(dataname)
    save_data(data, dataname)


def save_data(dataframe, filename):
    """Create a data folder in your current dir"""
    dataframe.to_csv("./data/" + filename + ".csv")


# This loop will iterate over ticker list, will pass one ticker to get
# data, and save that data as file.
for tik in ticker_list:
    get_data(tik)

TICKER_ITEMS = len(ticker_list)
for i in range(TICKER_ITEMS):
    df1 = pd.read_csv(f"./data/{str(files[i])}.csv")
    print(df1.head())
