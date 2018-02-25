import tweepy
import csv
import sys

consumer_key = "zgxU0sbLkEB93I3I3wLEDjRok"
consumer_secret = "nmV0Q8bNsNsFlKffVKbNy20vX2IAWNtzLbcHpNsZaoYAysgxfI"

access_token = "961470586827440128-EFWGLphaPXOUQkjCZNjzcdgXfmtTYcy"
access_token_secret = "TZFVLqznwo6lgITQlVk6T9lxIKaAimV7WShXVnYItnFYL"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Open/Create a file to append data
csvFile = open(sys.argv[0]+'tweets.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)


for tweet in tweepy.Cursor(api.search,q=sys.argv[0], lang="en", since_id="2017-19-02").items():
    print(tweet.created_at, tweet.text)
    follower_count = tweet.user.followers_count
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),follower_count])
