import pandas as pd 
import datetime as dt 
from pandas_datareader import data as pdr
import numpy as np 
import matplotlib.pyplot as plt
import yfinance as yf



def get_data(stocks, start, end ):
    stockData = yf.download(stocks, start= startDate, end= endDate)
    stockData = stockData["Close"]
    returns = stockData.pct_change()
    meanReturns = returns.mean()
    covMatrix = returns.cov()
    return meanReturns, covMatrix




# this is the  stocks that are searched through Y Finance stock data 
stocks = ["SPY"]
# endDate is the current data as is
endDate = dt.datetime.now()
#startDate = Current Date - dt Delta Time 300 days #! days is good number to mess with 
startDate = endDate - dt.timedelta(days= 300)
# this takes the meanReturns and takes the covariance Matrix which stores data
meanReturns, covMatrix = get_data(stocks, startDate, endDate)
print(meanReturns)# this creates the shape of the matrix, this is important because it assigns random weightings and has no bias

weights = np.random.random(len(meanReturns))
weights /= np.sum(weights)

print(weights)

mc_sims = 1000 #! great numbers to test out number of simulations the it will run 
T = 365 # timeframe in days 

meanM = np.full(shape= (T, len(weights)), fill_value = meanReturns)
meanM = meanM.T 

portfolio_sims = np.full(shape = (T, mc_sims), fill_value= 0.0)

initialPortfolio = 100000 # this is the number assigned to the portfolio initally

for m in range(0, mc_sims):  #? T = Timeframe in days 
    #MC Loops       #?      (T * Number of stocks we have) 
    Z = np.random.normal(size=(T, len(weights)))
    L = np.linalg.cholesky(covMatrix) #! finds lower triangle for Cholesky Decompesition
    dailyReturns = meanM + np.inner(L, Z)
    portfolio_sims[:,m] = np.cumprod(np.inner(weights, dailyReturns.T)+1)*initialPortfolio # This accounts for the cumlative effect of daily Return

plt.plot(portfolio_sims)
plt.ylabel("Portfolio Value ($)")
plt.xlabel("Days")
plt.title("MC simulation of a stock portfolio")
plt.show()