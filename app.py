from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
  return "angrycorner. We tell you what to be angry about so you don't have too. Never feel left out again in your anger."

if __name__ == "__main__":
  app.run()
