import tweepy
import csv
import sys
import datetime

consumer_key = "zgxU0sbLkEB93I3I3wLEDjRok"
consumer_secret = "nmV0Q8bNsNsFlKffVKbNy20vX2IAWNtzLbcHpNsZaoYAysgxfI"

access_token = "961470586827440128-EFWGLphaPXOUQkjCZNjzcdgXfmtTYcy"
access_token_secret = "TZFVLqznwo6lgITQlVk6T9lxIKaAimV7WShXVnYItnFYL"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Open/Create a file to append data
csvFile = open('tweetdata/'+sys.argv[1]+'tweets.csv', 'a')
#Use csv Writer
fields = ('date','text', 'followers')
csvWriter = csv.writer(csvFile, lineterminator= '\n')

for tweet in tweepy.Cursor(api.search,q=sys.argv[1], lang="en", since_id="2018-2-23").items():
    print(tweet.created_at, tweet.text)
    follower_count = tweet.user.followers_count
    #if tweet.created_at >= datetime.datetime(2019,2,24):
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),follower_count])
