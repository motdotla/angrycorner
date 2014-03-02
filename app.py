import os
from angrycorner import app

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)


from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
  return "angrycorner. We tell you what to be angry about so you don't have too. Never feel left out again in your anger."

if __name__ == "__main__":
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
