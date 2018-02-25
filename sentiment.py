import textblob
import tweepy
import pandas
import sys
from textblob import TextBlob

consumer_key = "zgxU0sbLkEB93I3I3wLEDjRok"
consumer_secret = "nmV0Q8bNsNsFlKffVKbNy20vX2IAWNtzLbcHpNsZaoYAysgxfI"

access_token = "961470586827440128-EFWGLphaPXOUQkjCZNjzcdgXfmtTYcy"
access_token_secret = "TZFVLqznwo6lgITQlVk6T9lxIKaAimV7WShXVnYItnFYL"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret,)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
colnames=['date', 'text', 'followers']

df = pandas.read_csv('tweetdata/'+sys.argv[1]+'tweets.csv',encoding='latin-1', names=colnames, header=None)
df['polarity'] = 0.0000
df['sentiment_confidence'] = 0.0000

for index,row in df.iterrows():
    analysis = TextBlob(df['text'][index])
    sentiment, confidence = analysis.sentiment
    df.at[index,'polarity'] = sentiment
    df.at[index,'sentiment_confidence'] = confidence

df.to_csv('sentimentdata/'+sys.argv[1]+'sentiment.csv')
