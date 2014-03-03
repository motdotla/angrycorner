from classifier import AngryClassifier

classifier = AngryClassifier()
print classifier.classify_tweet("This is a wonderful bus trip")
print classifier.classify_many(["I am angry at this bus trip", 
                                 "what is a bus trip anyway?"])
