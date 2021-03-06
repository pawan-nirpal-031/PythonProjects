import nltk
from nltk.corpus import twitter_samples
import matplotlib.pyplot as plt
from nltk.util import print_string
import numpy as np
import random
import re
import string
from nltk.corpus import stopwords          # module for stop words that come with NLTK
from nltk.stem import PorterStemmer        # module for stemming
from nltk.tokenize import TweetTokenizer   # module for tokenizing strings
import numpy as np
from utils import process_tweet

all_postive = twitter_samples.strings('positive_tweets.json')
all_negetive = twitter_samples.strings('negative_tweets.json')

def Clean(all_postive,all_negetive):
    postive = []
    negetive = []
    for tweet in all_postive:
        t1 = re.sub(r'^RT[\s]+', '', tweet)
        t2 =  re.sub(r'https?:\/\/.*[\r\n]*', '', t1)
        postive.append(re.sub(r'#', '', t2))
    for tweet in all_negetive:
        t1 = re.sub(r'^RT[\s]+', '', tweet)
        t2 =  re.sub(r'https?:\/\/.*[\r\n]*', '', t1)
        negetive.append(re.sub(r'#', '', t2))
    return postive,negetive

def TokenizeTweet(tweet):
    token =  TweetTokenizer(preserve_case=False, strip_handles=True,
                               reduce_len=True)
    return token.tokenize(tweet)
    

def PieChart(all_postive,all_negetive):
    fig = plt.figure(figsize=(5,5))
    labels = 'positive','negetive'
    sizes = [len(all_postive),len(all_negetive)]
    plt.pie(sizes,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
    plt.axis('equal')
    plt.show()

def StopWordsClean(all_postive_clean,all_negetive_clean):
    pclean =[]
    nclean =[]
    stopwords_eng = stopwords.words('english')
    punct = string.punctuation
    
    for ptweet in all_postive_clean:
        cleased_token =[]
        stemmed_tweet = StemTweet(TokenizeTweet(ptweet))
        for word in stemmed_tweet:
            if( word not in stopwords_eng and word not in punct):
                cleased_token.append(word)
        pclean.append(cleased_token)
    
    for ptweet in all_negetive_clean:
        cleased_token =[]
        stemmed_tweet = StemTweet(TokenizeTweet(ptweet))
        for word in stemmed_tweet:
            if( word not in stopwords_eng and word not in punct):
                cleased_token.append(word)
        nclean.append(cleased_token)
    
    return pclean,nclean

def StemTweet(tweet):
    stemmer = PorterStemmer()
    tweet_stem =[]
    for word in tweet:
        tweet_stem.append(stemmer.stem(word))
    return tweet_stem


cleansed = Clean(all_postive,all_negetive)
all_negetive_clean = cleansed[1]
all_postive_clean = cleansed[0]

stclean = StopWordsClean(all_postive_clean,all_negetive_clean)

all_postive_clean = stclean[0]
all_negetive_clean = stclean[1]
def process_tweet(tweet):
    stemmer = PorterStemmer()
    stopwords_english = stopwords.words('english')
    tweet = re.sub(r'\$\w*', '', tweet)
    tweet = re.sub(r'^RT[\s]+', '', tweet)
    tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)
    tweet = re.sub(r'#', '', tweet)
    tokenizer = TweetTokenizer(preserve_case=False,        strip_handles=True,reduce_len=True)
    tweet_tokens = tokenizer.tokenize(tweet)

    tweets_clean = []
    for word in tweet_tokens:
        if (word not in stopwords_english and  
                word not in string.punctuation): 
            stem_word = stemmer.stem(word)  # stemming word
            tweets_clean.append(stem_word)

    return tweets_clean

def build_freqs(tweets, ys):
    """Build frequencies.
    Input:
        tweets: a list of tweets
        ys: an m x 1 array with the sentiment label of each tweet
            (either 0 or 1)
    Output:
        freqs: a dictionary mapping each (word, sentiment) pair to its
        frequency
    """
    # Convert np array to list since zip needs an iterable.
    # The squeeze is necessary or the list ends up with one element.
    # Also note that this is just a NOP if ys is already a list.
    yslist = np.squeeze(ys).tolist()

    # Start with an empty dictionary and populate it by looping over all tweets
    # and over all processed words in each tweet.
    freqs = {}
    for y, tweet in zip(yslist, tweets):
        for word in process_tweet(tweet):
            pair = (word, y)
            if pair in freqs:
                freqs[pair] += 1
            else:
                freqs[pair] = 1    
    return freqs

