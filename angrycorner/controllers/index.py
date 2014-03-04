from angrycorner import app
from flask import abort, request, make_response
from angrycorner.views.mobile import MobileViews

@app.route('/')
def mobile_index():
  mobile_views = MobileViews()

  return mobile_views.draw_index()

@app.route('/result')
def mobile_result():
  mobile_views = MobileViews()

  return mobile_views.draw_result()

