from flask import Flask

app = Flask(__name__)

from angrycorner.controllers import index

