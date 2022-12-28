import ta
import yfinance as yf
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

#Start
def get_tct():
  print('---------------------------------')
  print('--write your token abbreviation--')
  print('------------Example:-------------')
  print('-------BTC/ETH/VAI/SPOT----------')  
  print('---------------------------------')
  ticker = input('CTA~#: ')
  #ticker = 'SOL'
  ticker = ticker+'-USD'
  return ticker

def get_data(ticker):
    token = yf.Ticker(ticker)
    data = token.history(period="5d",interval="1m")
    return data    

#EMA
def EMA(data):
  ema = ta.trend.EMAIndicator(data['Close'], window = 200).ema_indicator() 
  return ema


# MACD
def MACD(data):
  # # Calculate MACD values using the pandas_ta library
  # df.ta.macd(close='close', fast=12, slow=26, signal=9, append=True)
  # Get the 26-day EMA of the closing price
  k = data.ewm(span=12, adjust=False, min_periods=12).mean()
  # Get the 12-day EMA of the closing price
  d = data.ewm(span=26, adjust=False, min_periods=26).mean()
  # Subtract the 26-day EMA from the 12-Day EMA to get the MACD
  macd1 = k - d
  # Get the 9-Day EMA of the MACD for the Trigger line
  macd_s = macd1.ewm(span=9, adjust=False, min_periods=9).mean()
  # Calculate the difference between the MACD - Trigger for the Convergence/Divergence value
  macd_h = macd1 - macd_s
  # Add all of our new values for the MACD to the dataframe

  # View our data
  pd.set_option("display.max_columns", None)
  '''print(macd1)
  print(macd_s)
  print(macd_h)'''

  macd = pd.concat([macd1['Close'],macd_s['Close'],macd_h['Close']], axis=1)
  macd.columns = ['fast', 'signal', 'Hystogram']
  return macd


def get_fdata(data, ema, macd):
    fdata = pd.concat([data['Close'], ema,macd], axis=1)
    fdata.columns = ['Price', 'EMA', 'fast', 'signal', 'Hystogram']
    return fdata    

















































