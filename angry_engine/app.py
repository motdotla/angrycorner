import os
#import predictor.demo
from flask import Flask, session, redirect, url_for, escape, request
import classifier.classifier

from classifier import AngryClassifier


app = Flask(__name__)
classifier = AngryClassifier()

@app.route('/single')
def classify_single():
    tweet = "string"
    sentiment = classifier.classify_tweet(tweet)
    return "angry or happy"

@app.route('/many')
def classify_many():
    tweets = ["string",
              "string"]
    sentiment = classifier.classify_tweets(tweets)
    return "something else"
