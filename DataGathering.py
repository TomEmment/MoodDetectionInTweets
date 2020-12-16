import string
import tweepy
import csv
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
####input your credentials here
consumer_key = 'X4GdKJsPC5FwUypV4R4yQWlWk'
consumer_secret = 'zF9m8Sra9lDnXC7iNkLG8AzT9ZlN7OblRqR64GdSuiPFiOg4TE'
access_token = '1318227698762874884-ahsWaaDBIjf0Zl9fnSST4OBmrG413O'
access_token_secret = '9Derhjj0xTXUXWCHxGyrYFCfYmZrRCApYQIkFIAGnFC42'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

csvFile = open('Sad.csv', 'a')

csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="Sad",count=1000,lang="en").items():
    # #Happy and #Sad good results due to word association
    # #IamHappy and #Iamsad tended to be longer winded sentances not ideal
    tokens = word_tokenize(str(tweet.text))
    tokens = [w.lower() for w in tokens]
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    words = [word for word in stripped if word.isalpha()]
    words = [w for w in words if not w in stop_words]

    words = ', '.join(words)
    #Neural Network
    #support verctor machines
    #Decision trees - adaboost chapter 5,6,7,10,11, maybe 16
    #chapter 7 andrew ng
    try:
        csvWriter.writerow([tweet.created_at, words, tweet.source])
    except:
        print("Error collecting data line")
csvFile.close()
