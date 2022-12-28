import yfinance as yf
import pandas as pd

b = yf.Ticker('ETH-USD')
a = b.history(period='max', interval='1d')


while True:
    token = yf.Ticker('ETH-USD')
    df = token.history(period='max', interval='1d')

    if df['Close'].iloc[-1] != a['Close'].iloc[-1]:
        a = df
        print('----changed----')
    else:
        print('---------------')   
