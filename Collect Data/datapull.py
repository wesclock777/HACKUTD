import pandas as pd
from pandas_datareader import data as web
# Package and modules for importing data; this code may change depending on pandas version
import datetime
import urllib
import csv

# We will look at stock prices over the past year, starting at January 1, 2016
start = datetime.datetime(2018,2,23)

# Let's get Apple stock data; Apple's ticker symbol is AAPL
# First argument is the series we want, second is the source ("yahoo" for Yahoo! Finance), third is the start date, fourth is the end date
apple = web.DataReader("AAPL", "google", start)
type(apple)
print(apple)
