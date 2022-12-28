import ta
import yfinance as yf
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
from func import *
    #getting a ticker
ticker = get_tct()

while True:
    #getting data
    data = get_data(ticker)
    # calculate our indicators
    ema = EMA(data)
    macd = MACD(data)    
    final_data = get_fdata(data, ema, macd)
