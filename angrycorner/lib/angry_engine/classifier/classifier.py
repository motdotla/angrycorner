import os
import csv
import nltk
import random

def load_dataset(filename, sentiment):
    current_dir   = os.path.dirname(__file__)
    rel_env_path  = "../"+filename
    abs_file_path = os.path.join(current_dir, rel_env_path)

    with open(abs_file_path, "rb") as csvfile:
        reader = csv.reader(csvfile)
        features = []
        for row in reader:
            features.append((dict([(word, True) for word in row[5].split(' ')]), sentiment))
        return features

def format_tweet(tweet):
    document_words = set(tweet.split(' '))
    return dict([(word, True) for word in tweet])


def get_trained_classifier(training_set):
    return nltk.NaiveBayesClassifier.train(training_set)



positive_train = "data/1000_happy.csv"
negative_train = "data/1000_angry.csv"



happy_set = load_dataset(positive_train, "happy")
angry_set = load_dataset(negative_train, "angry")
random.shuffle(happy_set)
random.shuffle(angry_set)

# 80-20 testing
#test_cutoff = int(len(happy_set)*.8)
#testing_set = happy_set[:test_cutoff] + angry_set[:test_cutoff]

#training_set = happy_set[test_cutoff:] + angry_set[test_cutoff:]
training_set = happy_set + angry_set

classifier = get_trained_classifier(training_set)

class AngryClassifier():
    classifier = get_trained_classifier(training_set)

    def classify_tweet(self,tweet):
        return self.classifier.classify(format_tweet(tweet.split()))

    def classify_tweets(self,tweets):
        sentiments = []
        for tweet in tweets:
            sentiments.append(self.classifier.classify(format_tweet(tweet)))
        if sentiments.count("happy") > sentiments.count("angry"):
            return "happy"
        else:
            return "angry"

    def normalize_happy_angry_values_from_tweets(self, tweets):
        current_value = 0
        values = []
        sentiments = []
        for tweet in tweets:
            sentiments.append(self.classifier.classify(format_tweet(tweet)))
            for sentiment in sentiments:
                if sentiment == "happy":
                    current_value = current_value + 1
                    current_value = min(current_value, 10)
                    values.append(current_value)
                else:
                    current_value = current_value - 1
                    current_value = max(current_value, -10)
                    values.append(current_value)

        return values
