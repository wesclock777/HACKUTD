import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
# python twitter_stream_download.py -q apple -d data
#
# It will produce the list of tweets for the query "apple"
# in the file data/stream_apple.json

consumer_key = "zgxU0sbLkEB93I3I3wLEDjRok"
consumer_secret = "nmV0Q8bNsNsFlKffVKbNy20vX2IAWNtzLbcHpNsZaoYAysgxfI"

access_token = "961470586827440128-EFWGLphaPXOUQkjCZNjzcdgXfmtTYcy"
access_token_secret = "TZFVLqznwo6lgITQlVk6T9lxIKaAimV7WShXVnYItnFYL"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret,)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class MyListener(StreamListener):
    def __init__(self):
        query_fname = "apple"
        self.outfile = query_fname+".json"
    def on_data(self, data):
        try:
            with open(self.outfile, 'a') as f:
                f.write(data)
                print(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


if __name__== '__main__':
    twitter_stream = Stream(auth, MyListener())
    twitter_stream.filter(track=['$APPL', 'Apple'])
    # activates a listener that feeds the relevant data into a json file in data
