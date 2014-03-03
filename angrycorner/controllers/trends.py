import os
import json
import urlparse
from angrycorner import app
from flask import abort, request, make_response
import angrycorner.lib.twitter_api as twitter_api

@app.route('/trends')
def trends():

  """ trends """
  twitter_api_key     = os.environ.get('TWITTER_API_KEY')
  twitter_api_secret  = os.environ.get('TWITTER_API_SECRET')
  api = twitter_api.Api(twitter_api_key, twitter_api_secret)

  latitude  = request.args.get('lat', '36.1667')
  longitude = request.args.get('long', '-86.7878')

  result    = api.get_trends_closest(latitude, longitude)
  woeid     = result[0]['woeid']

  result    = api.get_trends_place(woeid)

  return json.dumps(result)

  
@app.route('/trends/closest')
def trends_closest():

  """ trends/closest """

  twitter_api_key     = os.environ.get('TWITTER_API_KEY')
  twitter_api_secret  = os.environ.get('TWITTER_API_SECRET')
  api = twitter_api.Api(twitter_api_key, twitter_api_secret)

  latitude  = request.args.get('lat', '36.1667')
  longitude = request.args.get('long', '-86.7878')

  result = api.get_trends_closest(latitude, longitude)

  return json.dumps(result)

@app.route('/trends/place')
def trends_place():

  """ trends/place """

  twitter_api_key     = os.environ.get('TWITTER_API_KEY')
  twitter_api_secret  = os.environ.get('TWITTER_API_SECRET')
  api = twitter_api.Api(twitter_api_key, twitter_api_secret)

  woeid  = request.args.get('id', '2457170')

  result = api.get_trends_place(woeid)

  return json.dumps(result)
