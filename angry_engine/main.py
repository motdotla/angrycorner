import os
#import predictor.demo
from flask import Flask, session, redirect, url_for, escape, request
import classifier.classifier as angry_classifier

app = Flask(__name__)
classifier = angry_classifier.AngryClassifier()

@app.route('/single')
def classify_single():
    return "something!"
