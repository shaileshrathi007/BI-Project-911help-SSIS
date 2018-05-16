
from __future__ import print_function

from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, \
    CategoriesOptions, ConceptsOptions, EmotionOptions, \
    EntitiesOptions, KeywordsOptions, KeywordsOptions, \
    MetadataOptions, RelationsOptions, SemanticRolesOptions, SentimentOptions
import json
import nltk
import re
from nltk.corpus import stopwords
import pandas as pd

stopwords = set(nltk.corpus.stopwords.words('english'))

stopwords.update(['tweet', 'twitter', 'like', 'likes', 'retweet'])

import os
os.chdir('/media/viraj/New Volume/Work/DWBI/911/unstructured_data/IBM_STT/csv')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username='a216aaf0-2a1b-4cb0-8cfc-4790d7e85bc9',
    password='dq73kJzZO8C0')


stopwords = set(nltk.corpus.stopwords.words('english'))


def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


def ibm_nlu(data, filename):
    clean = [clean_tweet(tweet) for tweet in data['Text']]
    cleaned = [x for x in clean if x not in stopwords]
    # print(cleaned)
    response = natural_language_understanding.analyze(text=str(cleaned), features=Features(entities=EntitiesOptions(emotion=True, sentiment=True, limit=100), categories=CategoriesOptions(
    ), keywords=KeywordsOptions(sentiment=True, emotion=True, limit=100), relations=RelationsOptions(), semantic_roles=SemanticRolesOptions(), sentiment=SentimentOptions()))
    # print(json.dumps(response, indent=2))
    res = json.dumps(response, indent=2)
    filename = filename + '.json'
    file = open(filename, 'w')
    file.write(res)
    file.close


ibm_high = pd.read_csv('ibm_high.csv', sep=',', delimiter=None)
ibm_medium = pd.read_csv('ibm_medium.csv', sep=',', delimiter=None)
ibm_low = pd.read_csv('ibm_low.csv', sep=',', delimiter=None)


ibm_nlu(ibm_high,'ibm_high')
ibm_nlu(ibm_medium,'ibm_medium')
ibm_nlu(ibm_low,'ibm_low')


# tweetid = tweets['tweet_id'].unique().tolist()
# tweet = []

# for i in tweetid:
#     tweets['utrgv'] = tweet.append(i[0])

# print(tweets['utrgv'])

# print(tweets.groupby(tweets['tweet_id'])['Tweets'])

# ibm_nlu(tweets, 'NYCDCA')


print('IBM NLU Complete')