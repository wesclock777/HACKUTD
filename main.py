import tweepy
import csv
import sys

# PULLING TWEETS

consumer_key = "zgxU0sbLkEB93I3I3wLEDjRok"
consumer_secret = "nmV0Q8bNsNsFlKffVKbNy20vX2IAWNtzLbcHpNsZaoYAysgxfI"

access_token = "961470586827440128-EFWGLphaPXOUQkjCZNjzcdgXfmtTYcy"
access_token_secret = "TZFVLqznwo6lgITQlVk6T9lxIKaAimV7WShXVnYItnFYL"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Open/Create a file to append data
csvFile = open(sys.argv[1]+'tweets.csv', 'a')
#Use csv Writer
fields = ('date','text', 'followers')
csvWriter = csv.writer(csvFile, lineterminator= '\n')
csvWriter.writerow(['date','text','followers'])

for tweet in tweepy.Cursor(api.search,q=sys.argv[1], lang="en", since_id="2017-19-02").items():
    print(tweet.created_at, tweet.text)
    follower_count = tweet.user.followers_count
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),follower_count])

import pandas as pd
from scipy import stats
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
#from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv("applefinal.csv")
dfold = df
df = df.drop('text', 1)
print(df.head())
df = df.drop('index', 1)
df = df.drop('date', 1)
print(df.head())

df_tr = df
# select proper number of clusters
'''
Y = df[['followers']]
X = df[['polarity']]

Nc = range(1, 20)
kmeans = [KMeans(n_clusters=i) for i in Nc]
score = [kmeans[i].fit(Y).score(Y) for i in range(len(kmeans))]
plt.plot(Nc,score)
plt.xlabel('Number of Clusters')
plt.ylabel('Score')
plt.title('Elbow Curve')
plt.show()
'''

# elbow plot showed the point of dropoff to be around 5 clusters

#Standardize

clmns = ['followers', 'polarity', 'sentiment_confidence']

df_tr_std= stats.zscore(df_tr[clmns])

#Clustering

kmeans = KMeans(n_clusters=5, random_state=0).fit(df_tr_std)
labels = kmeans.labels_

#Glue back to original data
df_tr['clusters']=labels
dfold['clusters']=labels

clmns.extend(['clusters'])

print(df_tr[clmns].groupby(['clusters']).mean())

#Scatter plot of Wattage and Duration
sns.lmplot('polarity', 'sentiment_confidence',
           data=df_tr,
           fit_reg=False,
           hue="clusters",
           scatter_kws={"marker": "D",
                        "s": 20})

#dfold.to_csv('clusterdata/'+'apple'+'cluster.csv')
plt.title('tweets grouped by polarity and sentiment_confidence')
plt.xlabel('polarity')
plt.ylabel('sentiment_confidences')
plt.show()
