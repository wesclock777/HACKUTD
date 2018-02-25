import pandas as pd
from pandas_datareader import data as web
# Package and modules for importing data; this code may change depending on pandas version
import datetime
import sys


# Let's get Apple stock data; Apple's ticker symbol is AAPL
# First argument is the series we want, second is the source ("yahoo" for Yahoo! Finance), third is the start date, fourth is the end date

df = pd.read_csv("clusterdata/"+sys.argv[1]+"cluster.csv",index_col=0,encoding='latin-1')

def getstockvalue(change, followers, totalfollowers, polarity, confidence, currentprice):
    # determines effect of tweet on stock price change
    '''
    date = date.split()[0]
    date = date.split("/")
    start = datetime.datetime(int(date[2]),int(date[0]),int(date[1])-1)
    print(start)
    apple = web.DataReader("AAPL", "google", start)
    type(apple)
    print(apple)
    '''
    value = change*(followers/totalfollowers)*polarity*confidence/(currentprice)*10000
    print(value)
    return value

start = datetime.datetime(2018,2,23)
# Let's get Apple stock data; Apple's ticker symbol is AAPL
# First argument is the series we want, second is the source ("yahoo" for Yahoo! Finance), third is the start date, fourth is the end date
apple = web.DataReader(sys.argv[2], "google", start)
print(apple)
currentprice = apple['Open'][0]
dif = abs(apple['Open'][0] - apple['Close'][0])
print(dif)

totalfollowers = df['followers'].sum()

for index,row in df.iterrows():
    followers = df['followers'][index]
    polarity = df['polarity'][index]
    confidence = df['sentiment_confidence'][index]
    df.at[index,'difference'] = getstockvalue(dif, followers, totalfollowers, polarity, confidence, currentprice)

df.to_csv('finaldata/'+sys.argv[2]+'.csv')

print(df.head())
