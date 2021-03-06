import nltk
from nltk.corpus import twitter_samples
import matplotlib.pyplot as plt              # visualization library
import numpy as np 
from TwitterSentimentAnalysis import process_tweet,build_freqs
'''
process_tweet(): Cleans the text, tokenizes it into separate words, 
                 removes stopwords, and converts words to stems.
build_freqs(): This counts how often a word in the 'corpus' (the entire set of tweets)
                was associated with a positive label 1 or a negative label 0. It then builds 
                the freqs dictionary, where each key is a (word,label) tuple, and the value is the count 
                of its frequency within the corpus of tweets.
'''

