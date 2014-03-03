from flask import Flask
import os
from classifier import AngryClassifier

port = int(os.environ.get('PORT', 5000))

app = Flask(__name__)
app.run(host='0.0.0.0', port=port, debug=True)
classifier = AngryClassifier()


@app.route("/single")
def classify_single():
    return "hey"
    #status = classifier.classify_tweet("This bus is making me sleepy")
    #return status
    


