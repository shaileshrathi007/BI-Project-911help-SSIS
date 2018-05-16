import tweepy           
import pandas as pd     
import numpy as np      
from textblob import TextBlob
# For plotting and visualization:
#from IPython.display import display
#import matplotlib.pyplot as plt
#import seaborn as sns

''' Twitter Credentials'''
from textblob import TextBlob
import re
from unidecode import unidecode
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

CONSUMER_KEY    = 'Ali0tFk6wkmVrEJC0CgG9DUJb'
CONSUMER_SECRET = 'h8ZvtSvvzOTnfqFohzX6jJnfkcdatqo5ef1Nu7KGy7Y95GQwlQ'
ACCESS_TOKEN  = '871472195108843522-7Xvdm0cqzlH8mcEsg4QO94w6oJCM6rx'
ACCESS_SECRET = 'D7Dia2Y4MmSF3dnz5yOjcYpUVlgdaIEWTNsaWxKg67zLl'

df = pd.read_csv('tweet_id.csv', sep=',')

dep = df['tweet_id'].tolist()

print(dep[0])
def TwitterSetup():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

def clean_tweet(tweet):
  
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())



def analize_sentiment(tweet):
    '''
    Utility function to classify the polarity of a tweet
    using textblob.
    '''
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1


def tweets(dept, filename):
    extractor = TwitterSetup()
    analyzer = SentimentIntensityAnalyzer()
    tweets = extractor.user_timeline(screen_name=dept, count=200)
    for tweet in tweets[:200]:
        print(tweet.text)
    data = pd.DataFrame(data = [tweet.text for tweet in tweets[:200]], columns=['Tweets'])
    #data['len'] = np.array([len(tweet.text) for tweet in tweets])
    data['ID'] = np.array([tweet.id for tweet in tweets])
    data['Date'] = np.array([tweet.created_at for tweet in tweets])
    data['Source'] = np.array([tweet.source for tweet in tweets])
    data['Likes'] = np.array([tweet.favorite_count for tweet in tweets])
    #data['RTs'] = np.array([tweet.retweet_count for tweet in tweets])
    data['Sentiments'] = np.array([analize_sentiment(tweet) for tweet in data['Tweets']])
    #data['sents'] ='neg' lambda x: for sents in data['Sentiments'] == -1
    data['department'] = np.array(filename)
    #data = pd.concat([data['Tweets'], data['len'], data['ID'],
    #   data['Date'], data['Source'], data['Likes'],data['RTs'], data['Sentiments']]) 
    #data = pd.DataFrame(data, columns=['Tweets', 'len','ID','Date','Source','Likes','RTs','Sentiments'])
    #filename = filename + '.csv'
    return data

    #clean_tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
    #tweet = unidecode[data['Tweets']]
    #vs = analyzer.polarity_scores(tweet)
    #analysis = TextBlob(tweet)
    #sentiment = vs['compound']
    '''if analysis.sentiment.polarity > 0:
        return 1
    elif analysis.sentiment.polarity == 0:
        return 0
    else:
        return -1               
    data['sentiments'] = np.array([analize_sentiment(tweet) for tweet in data['Tweets']])'''
    #print(data.head(5))
    #print(sentiment)

df0 = tweets(dep[0],dep[0])
df1 = tweets(dep[1],dep[1])
df2 = tweets(dep[2],dep[2])
df3 = tweets(dep[3],dep[3])
# df5 = tweets(dep[4],dep[4])
# df6 = tweets(dep[5],dep[5])
# df7 = tweets(dep[6],dep[6])
# df8 = tweets(dep[7],dep[7])
# df9 = tweets(dep[8],dep[8])

frame = [df0,df1,df2,df3]
data = pd.concat(frame)
data.to_csv('twitter_sentiments.csv', index = False, encoding = 'utf-8')