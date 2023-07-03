from pandas_datareader import data as pdr
from datetime import date

import yfinance as yf
yf.pdr_override() 

import pandas as pd

# Tickers list
# We can add and delete any ticker from the list to get desired ticker live data
ticker_list=['BURE.ST', 'INDU-C.ST', 'KINV-B.ST', 'LATO-B.ST', 'INVE-B.ST']
today = date.today()

# We can get data by our choice by giving days bracket
start_date= "2023-01-01"
end_date=date.today()
files=[]

def getData(ticker):
 print (ticker)
 data = pdr.get_data_yahoo(ticker, start=start_date, end=today)
 dataname= ticker+'_'+str(today)
 files.append(dataname)
 SaveData(data, dataname)

# Create a data folder in your current dir.
def SaveData(df, filename):
 df.to_csv('./data/'+filename+'.csv')

#This loop will iterate over ticker list, will pass one ticker to get data, and save that data as file.
for tik in ticker_list:
 getData(tik)

ticker_items = len(ticker_list) - 1
for i in range(0,ticker_items):
 df1= pd.read_csv('./data/'+ str(files[i])+'.csv')
 print (df1.head())