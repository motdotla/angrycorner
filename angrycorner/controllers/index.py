from angrycorner import app
from flask import abort, request, make_response
from angrycorner.views.index import IndexViews

@app.route('/')
def index():

  """ index """

  index_views = IndexViews()

  return index_views.draw_index()

