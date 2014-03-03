from flask import Flask
from classifier import AngryClassifier

app = Flask(__name__)
classifier = AngryClassifier()


