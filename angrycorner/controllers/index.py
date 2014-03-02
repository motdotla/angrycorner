from angrycorner import app
from flask import abort, request, make_response

@app.route('/')
def index():
  return "angrycorner"
